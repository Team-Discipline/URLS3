from rest_framework.routers import DefaultRouter

from access_key.views import AccessKeyViewSet, CreateKeyViewSet

router = DefaultRouter()

router.register('apikey', CreateKeyViewSet)
router.register('', AccessKeyViewSet)

urlpatterns = router.urls
