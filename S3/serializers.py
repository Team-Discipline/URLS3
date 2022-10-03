from rest_framework import serializers

from S3.models import S3


class S3Serializer(serializers.ModelSerializer):
    issuer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    s3_url = serializers.URLField(read_only=True)
    security_result = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = S3
        fields = '__all__'


class S3HyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    issuer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    s3_url = serializers.URLField(read_only=True)

    class Meta:
        model = S3
        fields = '__all__'
