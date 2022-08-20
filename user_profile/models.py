from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Image(models.Model):
    uploaded_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='uploaded_image')
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.url


class UserProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    thumbnail = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
