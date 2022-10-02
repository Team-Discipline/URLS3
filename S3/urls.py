from django.urls import path

from S3.views import S3CreateGetViewSet, S3UpdateDeleteViewSet

urlpatterns = [
    path('', S3CreateGetViewSet.as_view()),
    path('<int:s3_id>/', S3UpdateDeleteViewSet.as_view())
]
