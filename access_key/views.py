from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey

from access_key.models import UserAccessKey
from access_key.serializers import GetUserAccessKeySerializer, CreateUserAccessKeySerializer


class AccessKeyViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = UserAccessKey.objects.all()
    serializer_class = GetUserAccessKeySerializer
    http_method_names = ['get']


class CreateKeyViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = UserAccessKey.objects.all()
    serializer_class = CreateUserAccessKeySerializer
    http_method_names = ['post']
