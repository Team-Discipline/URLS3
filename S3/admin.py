from django.contrib import admin

from S3.models import S3


@admin.register(S3)
class S3Admin(admin.ModelAdmin):
    list_display = ['id', 'issuer', 'target_url', 'created_at']
    search_fields = ['id', 'issuer', 'target_url']
