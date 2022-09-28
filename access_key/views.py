from datetime import timedelta

from django.utils import timezone
from django.utils.datetime_safe import datetime
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_api_key.models import APIKey

from access_key.serializers import AccessKeySerializer


class AccessKeyViewSet(mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = APIKey.objects.all()
    serializer_class = AccessKeySerializer
    http_method_names = ['post']

    def create(self, request: Request, *args, **kwargs):
        username = request.user.username

        try:
            APIKey.objects.get(name__exact=username).delete()
        except APIKey.DoesNotExist:
            ...

        api_key, key = APIKey.objects.create_key(name=request.user.username)
        expires = datetime.now(timezone.utc) + timedelta(days=90)
        api_key.expiry_date = expires
        api_key.save()

        s = self.get_serializer(api_key)

        return Response(s.data)
