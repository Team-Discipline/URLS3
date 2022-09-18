from rest_framework.routers import DefaultRouter

from analytics.views import AnalyticsViewSet, CollectDataViewSet

router = DefaultRouter()

router.register('collect', CollectDataViewSet, basename='collect_data')
router.register('', AnalyticsViewSet, basename='analytics')

urlpatterns = router.urls
