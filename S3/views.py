from rest_framework import viewsets, permissions

from S3.models import S3
from S3.serializers import S3Serializer


class S3ViewSet(viewsets.ModelViewSet):
    """
    When you generate S3.
    """
    queryset = S3.objects.all()
    serializer_class = S3Serializer
    permission_classes = [permissions.IsAuthenticated]
