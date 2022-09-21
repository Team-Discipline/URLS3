from django.contrib import admin

from analytics.models import CapturedData


@admin.register(CapturedData)
class CapturedUserDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address', 'referer_url', 'created_at']
    search_fields = ['id', 'ip_address', 'created_at']
