from rest_framework.routers import DefaultRouter
from urlvalidator.views import is_valid_url

router = DefaultRouter()

router.register('url', is_valid_url, basename='url')

urlpatterns = router.urls
