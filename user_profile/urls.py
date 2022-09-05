from rest_framework.routers import DefaultRouter

from user_profile.views import UserProfileViewSet, ImageViewSet

router = DefaultRouter()

router.register('image', ImageViewSet)
router.register('', UserProfileViewSet)

urlpatterns = router.urls
