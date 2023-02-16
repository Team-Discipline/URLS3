from django.urls import path

from analytics.views import AnalyticsView, UniqueVisitorsViewSet

urlpatterns = [
    path('<int:s3_id>/unique_visitors/', UniqueVisitorsViewSet.as_view()),
    path('<int:s3_id>/', AnalyticsView.as_view()),
]
