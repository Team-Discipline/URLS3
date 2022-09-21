from django.db import models


class CapturedData(models.Model):
    # TODO: S3 Information.
    # s3 = models.ForeignKey(S3k, on_delete=models.CASCADE, related_name='captured_data')
    # User's ip address.
    ip_address = models.GenericIPAddressField()
    # When JS collector is first loaded.
    js_reqeust_time_UTC = models.DateTimeField()
    # When ads page is fully loaded.
    page_loaded_time = models.DateTimeField()
    # When user is trying to leave ads page. `window.onbeforeunload`
    page_leave_time = models.DateTimeField()
    # URL before entered ads page.
    referer_url = models.URLField()
    # When `this` model is created. This field is created automatically.
    created_at = models.DateTimeField(auto_now_add=True)

    # User's location information
    country = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
