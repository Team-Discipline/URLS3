from django.contrib import admin

from analytics.models import CapturedData, UniqueVisitor


@admin.register(CapturedData)
class CapturedUserDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address', 's3', 'referer_url', 'created_at']
    search_fields = ['id', 'referer_url']
    list_filter = ['ip_address', 's3']
    list_select_related = True


@admin.register(UniqueVisitor)
class UniqueVisitorAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'created_at']
    search_fields = ['data', 'created_at']
    list_filter = ['data']
