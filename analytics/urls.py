from rest_framework.routers import DefaultRouter

from analytics.views import AnalyticsViewSet, CollectDataViewSet

router = DefaultRouter()

router.register('', AnalyticsViewSet, basename='analytics')
router.register('collect', CollectDataViewSet, basename='collect_data')

urlpatterns = router.urls
