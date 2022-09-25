from rest_framework import viewsets, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from S3.models import S3
from S3.serializers import S3Serializer
from urlvalidator.views import ValidateUrl

class S3ViewSet(viewsets.ModelViewSet):
    """
    When you generate S3.
    """
    queryset = S3.objects.all()
    serializer_class = S3Serializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request: Request, *args, **kwargs):
        if not request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        self.queryset = S3.objects.filter(issuer=request.user)
        return super().list(request, *args, **kwargs)

    def create(self, request: Request, *args, **kwargs):
        target_url = request.data['target_url']
        print(f'target_url: {target_url}')
        s3 = S3(issuer=request.user, target_url=target_url)
        s = S3Serializer(s3, context={'request': request})

        ValidateUrl.is_valid_url(request)
        '''
        Here to inject `security` checks and some of validations. 
        '''

        s3.s3_url = 'https://test.url/'

        s3.save()
        return Response(s.data)
