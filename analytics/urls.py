from django.urls import path

from analytics.views import AnalyticsViewSet, UniqueVisitorsViewSet

urlpatterns = [
    path('<int:s3_id>/unique_visitors/', UniqueVisitorsViewSet.as_view()),
    path('<int:s3_id>/', AnalyticsViewSet.as_view()),
]
