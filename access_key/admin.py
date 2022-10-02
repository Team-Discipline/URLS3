from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin

from access_key.models import UsualAPIKey


@admin.register(UsualAPIKey)
class UsualAPIKeyAdmin(APIKeyModelAdmin):
    list_display = ['user', 'key', 'expiry_date']
    search_fields = list_display
