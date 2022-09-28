from rest_framework.routers import DefaultRouter

from access_key.views import AccessKeyViewSet

router = DefaultRouter()

router.register('', AccessKeyViewSet)

urlpatterns = router.urls
