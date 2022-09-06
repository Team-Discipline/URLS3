from rest_framework.routers import DefaultRouter

from S3.views import S3ViewSet

router = DefaultRouter()

router.register('', S3ViewSet, basename='s3')

urlpatterns = router.urls
