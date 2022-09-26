from django.test import TestCase
from urlvalidator.views import ValidateUrl
from urlvalidator.models import URLModel


# Create your tests here.


class URLvalidationTestCase(TestCase):
    def test_url_validation(self):
        url1 = URLModel(url="https://www.google.com/?gws_rd=ssl").save()
        ValidateUrl.is_valid_url(self, url1)
