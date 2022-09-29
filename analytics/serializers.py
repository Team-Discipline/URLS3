from rest_framework import serializers

from S3.models import S3
from analytics.models import CapturedData


class CreateCapturedDataSerializer(serializers.HyperlinkedModelSerializer):
    s3 = serializers.PrimaryKeyRelatedField(queryset=S3.objects.all())

    class Meta:
        model = CapturedData
        exclude = ['ip_address', 'country', 'city', 'latitude', 'longitude', 'url']


class GetCapturedDataSerializer(serializers.ModelSerializer):
    ip_address = serializers.IPAddressField()

    class Meta:
        model = CapturedData
        fields = '__all__'
