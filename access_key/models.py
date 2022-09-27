from django.conf import settings
from django.db import models


class UserAccessKey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    access_key = models.CharField(max_length=1000)
    expires = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
