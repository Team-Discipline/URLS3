from rest_framework import serializers

from analytics.models import CapturedData


class CreateCapturedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturedData
        exclude = ['id', ]  # 's3']


class GetCapturedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturedData
        fields = '__all__'
