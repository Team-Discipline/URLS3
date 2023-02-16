from rest_framework import serializers

from S3.models import S3
from S3.serializers import S3GetSerializer
from analytics.models import CapturedData, UniqueVisitor


class CreateCapturedDataSerializer(serializers.HyperlinkedModelSerializer):
    s3 = serializers.HyperlinkedRelatedField(view_name='s3', queryset=S3.objects.all())

    class Meta:
        model = CapturedData
        exclude = ['ip_address', 'country', 'city', 'latitude', 'longitude', 'url']


class GetCapturedDataSerializer(serializers.ModelSerializer):
    # ip_address = serializers.IPAddressField()
    s3 = S3GetSerializer(many=False, read_only=True)

    class Meta:
        model = CapturedData
        fields = '__all__'


class UniqueVisitorSerializer(serializers.ModelSerializer):
    data = GetCapturedDataSerializer()

    class Meta:
        model = UniqueVisitor
        fields = '__all__'
