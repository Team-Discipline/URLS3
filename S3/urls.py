from django.urls import path

from S3.views import S3ViewSet, S3DeleteViewSet

urlpatterns = [
    path('', S3ViewSet.as_view()),
    path('<int:s3_id>/', S3DeleteViewSet.as_view())
]
