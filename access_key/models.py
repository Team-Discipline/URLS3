from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from rest_framework_api_key.models import APIKey


class UsualAPIKey(APIKey):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.user}\'s {self.key}'
