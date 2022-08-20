from rest_framework.routers import DefaultRouter

from user_profile.views import UserProfileViewSet, ImageViewSet

router = DefaultRouter()

router.register('image', ImageViewSet, basename='user_profile_image')
router.register('', UserProfileViewSet, basename='user_profile')

urlpatterns = router.urls
