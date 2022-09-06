from rest_framework import serializers

from S3.models import S3


class S3Serializer(serializers.HyperlinkedModelSerializer):
    issuer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = S3
        fields = '__all__'
