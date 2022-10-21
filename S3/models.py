from django.conf import settings
from django.core.validators import URLValidator
from django.db import models


class S3SecurityResult(models.Model):
    has_hsts = models.BooleanField()

    class Meta:
        verbose_name = 'Security Result'
        verbose_name_plural = 'Security Results'

    def __str__(self):
        return f'{self.s3.issuer}\'s {self.s3.target_url}'


class S3(models.Model):
    issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issued_s3')
    target_url = models.URLField(validators=[URLValidator])
    s3_url = models.URLField(unique=True, validators=[URLValidator])  # url that converted by URLS3.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    security_result = models.OneToOneField(S3SecurityResult,
                                           on_delete=models.SET_NULL,
                                           null=True,
                                           default=None,
                                           related_name='s3')

    def __str__(self):
        return f'{self.issuer}\'s shorten {self.target_url}'


class Word(models.Model):
    """
    This model (table) only get from admin panel.
    No plan to implement in `views.py`.
    """
    word = models.TextField(max_length=100)
    is_noun = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.word} ({self.is_noun})'
