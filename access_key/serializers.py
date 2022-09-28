from rest_framework import serializers

from rest_framework_api_key.models import APIKey


class CreateUserAccessKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey


class GetUserAccessKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = '__all__'
