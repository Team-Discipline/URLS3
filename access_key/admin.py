from django.contrib import admin

from access_key.models import UserAccessKey


@admin.register(UserAccessKey)
class UserAccessKeyAdmin(admin.ModelAdmin):
    list_filter = ['id', 'user', 'access_key', 'expires', 'created_at']
    search_fields = list_filter
