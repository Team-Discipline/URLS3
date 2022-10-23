from datetime import datetime

import requests
from rest_framework import throttling, generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

from S3.models import S3, S3SecurityResult, CombinedWords
from S3.serializers import S3Serializer
from S3.utils.CombineWords import get_combined_words
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
        """
        short_by_words = request.data.get('short_by_words')
        combined_words: CombinedWords | None = None

        if short_by_words:
            print(f'{short_by_words=}')
            combined_words: CombinedWords = get_combined_words()
            print(f'{combined_words=}')
            shortener_url = f'https://urls3.kreimben.com/{combined_words}'
        else:
            # TODO: Implement hashed url.
            shortener_url = f'https://urls3.kreimben.com/{datetime.now()}'

        s = S3Serializer(data=request.data, context={'request': request})

        if s.is_valid():
            '''
            Here to inject `security` checks and some of validations.
            '''
            try:
                result: S3SecurityResult = URLSecurityChecker.check(request.data.get('target_url'))

                user = find_user(request)
                s.save(issuer=user, s3_url=shortener_url, security_result=result)
                return Response(s.data)
            except requests.exceptions.ConnectionError:
                return Response({
                    'success': False,
                    'message': 'Can not connect with your given url!'
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(s.errors)


class S3UpdateDeleteViewSet(generics.DestroyAPIView,
                            generics.UpdateAPIView):
    queryset = S3.objects.all()
    serializer_class = S3Serializer
    permission_classes = [IsAuthenticated | HasAPIKey]
    throttle_classes = [throttling.UserRateThrottle]
    http_method_names = ['patch', 'delete']

    def update(self, request, *args, **kwargs):
        s3_id = kwargs['s3_id']

        if not s3_id:
            return Response({'success': False, 'message': 'ID is not filled.'}, status=status.HTTP_404_NOT_FOUND)

        s3 = get_object_or_404(S3, pk=s3_id)

        s3.target_url = request.data.get('target_url')
        s3.save()

        s = self.get_serializer(s3)

        return Response(s.data)

    def delete(self, request: Request, *args, **kwargs):
        s3_id = kwargs['s3_id']

        if not s3_id:
            return Response({'success': False, 'message': 'ID is not filled.'}, status=status.HTTP_404_NOT_FOUND)

        s3 = get_object_or_404(S3, pk=s3_id)

        s3.delete()
        return Response({'success': True, 'message': 'Successfully deleted!'}, status=status.HTTP_200_OK)
