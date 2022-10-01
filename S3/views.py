from datetime import datetime

from rest_framework import permissions, throttling, generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

from S3.models import S3
from S3.serializers import S3Serializer


class S3ViewSet(generics.ListCreateAPIView):
    """
    When you generate S3.
    """
    queryset = S3.objects.all()
    serializer_class = S3Serializer
    permission_classes = [permissions.IsAuthenticated | HasAPIKey]
    throttle_classes = [throttling.UserRateThrottle]
    http_method_names = ['get', 'post', 'patch']

    def get(self, request: Request, *args, **kwargs):
        """
        You can get only what you generated!
        """
        if not request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        self.queryset = S3.objects.filter(issuer=request.user)

        s = self.get_serializer(self.queryset, many=True, context={'request': request})

        return Response(s.data)

    def post(self, request: Request, *args, **kwargs):
        # target_url = request.data['target_url']
        # s3 = S3(issuer=request.user, target_url=target_url)
        data = request.data
        data['issuer_id'] = request.user.id
        print(f'request data: {request.data}')

        s = S3Serializer(data=request.data, context={'request': request})

        '''
        Here to inject `security` checks and some of validations.
        '''
        # URLSecurityChecker(target_url)

        """
        Here to generate S3 shortener url.
        """
        s.s3_url = f'https://test.url/{datetime.now()}'

        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)


class S3DeleteViewSet(generics.DestroyAPIView,
                      generics.UpdateAPIView):
    queryset = S3.objects.all()
    serializer_class = S3Serializer
    permission_classes = [permissions.IsAuthenticated | HasAPIKey]
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
