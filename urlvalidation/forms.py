from django import forms
from .models import ValidationCheck


class PostForm(forms.ModelForm):
    class Meta:
        model = ValidationCheck
        fields = '__all__'
