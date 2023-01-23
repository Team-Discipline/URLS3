from rest_framework import serializers

from S3.models import S3, Hash


class HashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hash
        fields = '__all__'
        read_only_fields = ['id', 'target_url', 'hash_value']


class S3CreateSerializer(serializers.Serializer):
    """
    It is just kind of form when generate S3.
    """
    target_url = serializers.URLField()
    short_by_words = serializers.BooleanField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class S3GetSerializer(serializers.ModelSerializer):
    """
    This is real serializer about S3 object.
    """
    issuer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    s3_url = serializers.URLField(read_only=True)
    security_result = serializers.PrimaryKeyRelatedField(read_only=True)
    short_by_words = serializers.SerializerMethodField()
    hashed_value = HashSerializer(read_only=True)

    def get_short_by_words(self, obj: S3):
        if '-' in obj.s3_url:
            return True
        else:
            return False

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
        exclude = ['updated_at', 'combined_words']


class S3HyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    """
    When related-url is needed.
    """
    issuer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    s3_url = serializers.URLField(read_only=True)

    class Meta:
        model = S3
        fields = '__all__'
