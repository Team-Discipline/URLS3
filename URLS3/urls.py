import os

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(f"{os.getenv('DJANGO_REAL_ADMIN')}", admin.site.urls),
    path('docs/', schema_view.with_ui(cache_timeout=0), name='schema-json'),
    path('token/', include('login.urls')),
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
]
