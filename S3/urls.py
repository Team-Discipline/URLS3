from django.urls import path

from S3.views import S3CreateGetViewSet, S3UpdateDeleteViewSet, find_hash_by_combined_words

urlpatterns = [
    path('', S3CreateGetViewSet.as_view(), name='s3'),
    path('find/', find_hash_by_combined_words, name='find_by_combined_word'),
    path('<str:hashed_value>/', S3UpdateDeleteViewSet.as_view(), name='s3-update-delete')
]
