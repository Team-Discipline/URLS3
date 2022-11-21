from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from S3.models import S3, S3SecurityResult, Word, CombinedWord, Hash


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
    list_filter = ['is_noun']
    actions = ['make_noun', 'make_adj']
    ordering = ['id', 'word']

    def make_noun(self, request: HttpRequest, queryset: QuerySet):
        updated_count = queryset.update(is_noun=True)
        self.message_user(request, f'{updated_count}개의 단어가 명사로 변경 됨.')

    make_noun.short_description = '선택한 단어들을 명사로 바꿈'

    def make_adj(self, request: HttpRequest, queryset: QuerySet):
        updated_count = queryset.update(is_noun=False)
        self.message_user(request, f'{updated_count}개의 단어가 형용사로 변경 됨.')

    make_adj.short_description = '선택한 단어들을 형용사로 바꿈'


@admin.register(CombinedWord)
class CombinedWordAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_word', 'second_word']
    search_fields = ['id', 'first_word', 'second_word']
    ordering = ['id']


@admin.register(Hash)
class HashAdmin(admin.ModelAdmin):
    list_display = ['id', 'target_url', 'hash_value']
    search_fields = ['id', 'target_url', 'hash_value']
    ordering = ['id']
