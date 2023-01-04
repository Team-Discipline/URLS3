from rest_framework import serializers

from S3.models import S3, Hash


class HashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hash
        fields = '__all__'
        read_only_fields = ['id', 'target_url', 'hash_value']


class S3Serializer(serializers.ModelSerializer):
    """
    When needed to s3. (just usual case)
    """
    issuer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    s3_url = serializers.URLField(read_only=True)
    security_result = serializers.PrimaryKeyRelatedField(read_only=True)
    short_by_words = serializers.BooleanField(read_only=False, default=True)
    hashed_value = HashSerializer(read_only=True)

    def create(self, validated_data: dict):
        """
        To filter `short_by_words` field
        because `short_by_words` is only for input data.
        Not row data (model)
        """
        new_validated_data = dict()
        for k, v in validated_data.items():
            if k != 'short_by_words':
                new_validated_data[k] = v
        return S3.objects.create(**new_validated_data)

    class Meta:
        model = S3
        exclude = ['created_at', 'updated_at', 'combined_words', 'is_ban']


class S3HyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    """
    When related-url is needed.
    """
    issuer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    s3_url = serializers.URLField(read_only=True)

    class Meta:
        model = S3
        fields = '__all__'
