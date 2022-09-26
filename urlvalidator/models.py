from django.db import models


class URLModel(models.Model):
    objects = None
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.url
