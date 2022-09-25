from django.test import TestCase
from urlvalidator.views import is_valid_url
from urlvalidator.models import URLModel


# Create your tests here.

class URLvalidationTestCase(TestCase):
    def setUp(self) -> None:
        URLModel.objects.create(url="www.google.com")
