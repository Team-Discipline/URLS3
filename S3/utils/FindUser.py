from django.contrib.auth.models import User
from rest_framework.request import Request

from access_key.models import UsualAPIKey


def find_user(request: Request) -> User:
    if request.META.get("HTTP_AUTHORIZATION") and request.META["HTTP_AUTHORIZATION"].split()[0] == 'Api-Key':
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        apikey = UsualAPIKey.objects.get_from_key(key)
        return apikey.user
    else:
        return request.user
