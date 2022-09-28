from rest_framework import serializers

from rest_framework_api_key.models import APIKey


class AccessKeySerializer(serializers.ModelSerializer):
    expiry_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = APIKey
        fields = ['hashed_key', 'expiry_date']
