from rest_framework import serializers

from access_key.models import UsualAPIKey


class AccessKeySerializer(serializers.ModelSerializer):
    key = serializers.CharField(read_only=True)
    revoked = serializers.BooleanField(read_only=True)
    expiry_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UsualAPIKey
        fields = ['key', 'revoked', 'expiry_date']
