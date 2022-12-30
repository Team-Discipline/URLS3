from django.db import models

from S3.models import S3


class CapturedData(models.Model):
    s3 = models.ForeignKey(S3, on_delete=models.CASCADE, related_name='captured_data')
    # User's ip address.
    ip_address = models.GenericIPAddressField()
    # When JS collector is first loaded.
    js_request_time_UTC = models.DateTimeField()
    # When ads page is fully loaded.
    page_loaded_time = models.DateTimeField()
    # When user is trying to leave ads page. `window.onbeforeunload`
    page_leave_time = models.DateTimeField()
    # URL before entered ads page.
    referer_url = models.URLField()
    # When `this` model is created. This field is created automatically.
    created_at = models.DateTimeField(auto_now_add=True)

    # User's location information
    country = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=1000, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.ip_address} ({self.s3})'


class UniqueVisitor(models.Model):
    """
    There is no way to input to this model.
    This model will be filled automatically.
    """
    data = models.ForeignKey(CapturedData, on_delete=models.CASCADE, related_name='unique_visitors')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.data.ip_address} on {self.data.created_at}'
