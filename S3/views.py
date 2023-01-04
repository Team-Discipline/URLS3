from datetime import datetime
from hashlib import md5

import requests
from django.http import HttpResponse, JsonResponse
from rest_framework import throttling, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

from S3.models import S3, S3SecurityResult, CombinedWord, Hash
from S3.serializers import S3Serializer
from S3.utils.CombineWord import get_combined_words
from S3.utils.FindUser import find_user
from S3.utils.URLSecurityChecker import URLSecurityChecker


class S3CreateGetViewSet(generics.ListCreateAPIView):
    """
    When you generate S3.
    """
    queryset = S3.objects.all()
    serializer_class = S3Serializer
    permission_classes = [IsAuthenticated | HasAPIKey]
    throttle_classes = [throttling.UserRateThrottle]
    http_method_names = ['get', 'post']

    def get(self, request: Request, *args, **kwargs):
        """
        You can get only what you generated!
        """
        user = find_user(request)
        self.queryset = S3.objects.filter(issuer=user)
        s = self.get_serializer(self.queryset, many=True, context={'request': request})

        return Response(s.data)

    def post(self, request: Request, *args, **kwargs):
        """
        Here to generate S3 shortener url.
        두 단어의 조합으로 url을 단축하려면 `short_by_words`에 true를 넣으면 됨.
        일반적인 hash키로 url을 단축하려면 `short_by_words`에 false를 넣으면 됨.
        문서에서 테스트 할 때 기본으로 `hashed_value`값 들어가는데, 이거 완전히 지우고 (기존처럼) request 보내면 됨.
        """
        short_by_words = request.data.get('short_by_words')

        combined_words: CombinedWord | None = None

        target_url = request.data.get('target_url')
        composite = target_url + str(datetime.now()) + request.user.username
        hash_value = md5(composite.encode("UTF-8")).hexdigest()[0:6]

        h = Hash(
            target_url=target_url,
            hash_value=hash_value,
        )

        h.save()

        if short_by_words:
            combined_words: CombinedWord = get_combined_words()
            shortener_url = f'https://urls3.kreimben.com/{combined_words}'
        else:
            shortener_url = f'https://urls3.kreimben.com/{hash_value}'

        serializer = self.get_serializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            '''
            Here to inject `security` checks and some of validations.
            '''
            try:
                result: S3SecurityResult = URLSecurityChecker.check(request.data.get('target_url'))

                user = find_user(request)
                serializer.save(issuer=user,
                                s3_url=shortener_url,
                                security_result=result,
                                combined_words=combined_words,
                                hashed_value=h
                                )
                serializer.short_by_words = short_by_words
                serializer.save()
                return Response(serializer.data)
            except requests.exceptions.ConnectionError:
                return Response({
                    'success': False,
                    'message': 'Can not connect with your given url!'
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors)


class S3UpdateDeleteViewSet(generics.DestroyAPIView,
                            generics.UpdateAPIView):
    queryset = S3.objects.all()
    serializer_class = S3Serializer
    permission_classes = [IsAuthenticated | HasAPIKey]
    throttle_classes = [throttling.UserRateThrottle]
    http_method_names = ['patch', 'delete']
    lookup_field = 'hashed_value'

    def update(self, request, *args, **kwargs):
        print(f'{kwargs=}')
        hashed_value = kwargs['hashed_value']

        if not hashed_value:
            return Response({'success': False, 'message': 'ID is not filled.'}, status=status.HTTP_404_NOT_FOUND)

        s3 = get_object_or_404(S3, hashed_value__hash_value=hashed_value)

        s3.target_url = request.data.get('target_url')
        s3.save()

        s = self.get_serializer(s3)

        return Response(s.data)

    def delete(self, request: Request, *args, **kwargs):
        hashed_value = kwargs['hashed_value']

        if not hashed_value:
            return Response({'success': False, 'message': 'ID is not filled.'}, status=status.HTTP_404_NOT_FOUND)

        s3 = get_object_or_404(S3, hashed_value__hash_value=hashed_value)

        if s3.issuer != request.user:
            return Response({'message': "Not your S3 issued by you."}, status=status.HTTP_400_BAD_REQUEST)

        s3.delete()
        return Response({'success': True, 'message': 'Successfully deleted!'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([])
def find_hash_by_combined_words(request: Request):
    """
    body에 { "first_word": {first}, "second_word": {second} }를 입력하면 됩니다.
    단어 조합을 찾지 못한 경우에는 404 코드만 제공됩니다.
    """
    first_word = request.data.get('first_word')
    second_word = request.data.get('second_word')

    try:
        combined_word = CombinedWord.objects.select_related('s3') \
            .get(first_word__word=first_word, second_word__word=second_word)
    except CombinedWord.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if combined_word:
        value = combined_word.s3.hashed_value.hash_value

        return JsonResponse(status=status.HTTP_200_OK, data={'hashed_value': value})
