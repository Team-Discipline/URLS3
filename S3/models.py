from django.conf import settings
from django.db import models


class S3(models.Model):
    issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issued_s3')
    target_url = models.URLField()
    s3_url = models.URLField(unique=True)  # url that converted by URLS3.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.issuer}\'s {self.s3_url if self.s3_url is not None else self.target_url}'
