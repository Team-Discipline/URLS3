from django.contrib import admin

from user_profile.models import UserProfile, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'uploaded_by', 'image', 'created_at', 'updated_at']
    search_fields = ['id', 'uploaded_by']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'thumbnail', 'created_at', 'updated_at']
    search_fields = ['id', 'user']
