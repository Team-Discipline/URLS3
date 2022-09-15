from rest_framework import viewsets, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from S3.models import S3
from S3.serializers import S3Serializer


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
