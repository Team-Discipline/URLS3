from django.conf import settings
from django.core.validators import URLValidator
from django.db import models


class S3SecurityResult(models.Model):
    has_hsts = models.BooleanField()

    class Meta:
        verbose_name = 'Security Result'
        verbose_name_plural = 'Security Results'

    def __str__(self):
        if hasattr(self, 's3'):
            return f'{self.s3.issuer if self.s3 else "None"}\'s {self.s3.target_url}'
        else:
            return f'NA'


class Word(models.Model):
    """
    This model (table) only get from admin panel.
    No plan to implement in `views.py`.
    """
    word = models.TextField(max_length=100, unique=True)
    is_noun = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.word} ({"Noun" if self.is_noun else "Adj"})'


class CombinedWords(models.Model):
    first_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='first_words')
    second_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='second_words')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_word.word}-{self.second_word.word}'


class Hash(models.Model):
    origin_url = models.URLField(validators=[URLValidator])
    hash_value = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.hash_value}'


class S3(models.Model):
    issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issued_s3')
    hash = models.OneToOneField(Hash, on_delete=models.CASCADE, related_name='hash', default=None)
    target_url = models.URLField(validators=[URLValidator])
    s3_url = models.URLField(unique=True, validators=[URLValidator])  # url that converted by URLS3.
    combined_words = models.OneToOneField(CombinedWords, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_ban = models.BooleanField(default=False)
    security_result = models.OneToOneField(S3SecurityResult,
                                           on_delete=models.CASCADE,
                                           null=True,
                                           default=None,
                                           related_name='s3')

    def __str__(self):
        return f'{self.issuer}\'s shorten {self.target_url}'
