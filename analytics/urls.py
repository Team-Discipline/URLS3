from django.urls import path

from analytics.views import AnalyticsViewSet

urlpatterns = [
    path('<int:s3_id>/', AnalyticsViewSet.as_view())
]
