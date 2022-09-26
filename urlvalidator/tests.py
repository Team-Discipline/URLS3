from django.test import TestCase
from urlvalidator.views import ValidateUrl
from urlvalidator.models import URLModel


# Create your tests here.


class URLvalidationTestCase(TestCase):
    def test_url_validation(self):
        url = URLModel.objects.create(url="https://www.google.com/?gws_rd=ssl")
        ValidateUrl.is_valid_url(url)
