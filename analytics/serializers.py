from rest_framework import serializers

from S3.models import S3
from analytics.models import CapturedData


class CreateCapturedDataSerializer(serializers.HyperlinkedModelSerializer):
    s3_s3_url = serializers.HyperlinkedRelatedField(view_name='URLS3:s3-detail',
                                                    lookup_field='s3_url',
                                                    queryset=S3.objects.all())

    class Meta:
        model = CapturedData
        exclude = ['ip_address', 'country', 'city', 'latitude', 'longitude', 's3']
        extra_kwargs = {
            'url': {
                'view_name': 'captureddata-detail'
            }
        }


class GetCapturedDataSerializer(serializers.HyperlinkedModelSerializer):
    ip_address = serializers.IPAddressField()

    class Meta:
        model = CapturedData
        fields = '__all__'
