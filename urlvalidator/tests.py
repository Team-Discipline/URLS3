from django.test import TestCase
from urlvalidator.views import ValidateUrl
from urlvalidator.models import URLModel

# Create your tests here.


class URLvalidationTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self) -> None:
        pass

    def test_url_validation(self):
        url = URLModel.objects.create(url="www.google.com")
        ValidateUrl.is_valid_url(url)
