from django.contrib import admin

from analytics.models import CapturedData, UniqueVisitor


@admin.register(CapturedData)
class CapturedUserDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address', 'referer_url', 'created_at']
    search_fields = ['id', 'ip_address', 'referer_url', 'created_at']


@admin.register(UniqueVisitor)
class UniqueVisitorAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'created_at']
    search_fields = ['data', 'created_at']
