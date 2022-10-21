from django.contrib import admin

from S3.models import S3, S3SecurityResult, Word


@admin.register(S3)
class S3Admin(admin.ModelAdmin):
    list_display = ['id', 'issuer', 's3_url', 'target_url', 'created_at']
    search_fields = ['id', 'issuer', 's3_url', 'target_url']


@admin.register(S3SecurityResult)
class S3SecurityResultAdmin(admin.ModelAdmin):
    list_display = ['id', 's3', 'has_hsts']
    search_fields = ['id', 's3', 'has_hsts']


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['id', 'word', 'is_noun']
    search_fields = ['id', 'word', 'is_noun']
