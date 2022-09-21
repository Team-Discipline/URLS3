from rest_framework import serializers

from analytics.models import CapturedData


class CreateCapturedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturedData
        exclude = ['id', 'ip_address', 'country', 'city', 'latitude', 'longitude']  # 's3']


class GetCapturedDataSerializer(serializers.ModelSerializer):
    ip_address = serializers.IPAddressField()

    class Meta:
        model = CapturedData
        fields = '__all__'
