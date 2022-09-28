from datetime import datetime, timedelta

from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets, status, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_api_key.models import APIKey


class AccessKeyViewSet(mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = APIKey.objects.all()
    http_method_names = ['get']

    def apikey(self, request: Request):
        username = request.user.username

        response = {}

        keys = APIKey.objects.all()
        for key in keys:
            if key.name == username:
                response['access_key'] = key.prefix + '*****'
                response['expires'] = key.expiry_date
                response['created'] = key.created

        return Response(response, status=status.HTTP_200_OK)


class CreateKeyViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = APIKey.objects.all()
    http_method_names = ['post']

    def create(self, request: Request):
        username = request.user.username

        keys = APIKey.objects.all()
        for key in keys:
            if key.name == username:
                key.delete()
                break
        api_key, key = APIKey.objects.create_key(name=request.user.username)
        expires = datetime.now() + timedelta(days=90)
        api_key.expiry_date = expires
        api_key.save()

        return Response({'username': username, 'access_key': key, 'expires': expires}, status=status.HTTP_200_OK)
