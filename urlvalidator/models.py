from django.db import models


class URLModel(models.Model):
    # scheme = models.CharField(label="url_scheme")
    # netloc = models.CharField(label="url_netloc")
    # path = models.CharField(label="url_path")
    # hostname = models.CharField(label="url_hostname")
    # port = models.CharField(label="url_port")
    # params = models.CharField(label="url_params")
    # query = models.CharField(label="url_query")
    # fragment = models.CharField(label="url_fragment")
    url = models.URLField(max_length=200, blank=True)

