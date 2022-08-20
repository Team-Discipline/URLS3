import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="URLS3",
        default_version='0.1.0',
        description="Make URL Shortener, Securer, Sexier.",
    ),
    public=False,
    permission_classes=[permissions.IsAuthenticated],
)

urlpatterns = [
    path(f"{os.getenv('DJANGO_REAL_ADMIN')}", admin.site.urls),
    path('docs/', schema_view.with_ui(cache_timeout=0), name='schema-json'),
    path('token/', include('login.urls')),
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('profile/', include('user_profile.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
