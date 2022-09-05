from rest_framework import serializers

from user_profile.models import UserProfile, Image


class ImageSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'uploaded_by', 'image', 'created_at', 'updated_at']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    thumbnail = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='image-detail')

    class Meta:
        model = UserProfile
        fields = ['id', 'user_id', 'thumbnail', 'created_at', 'updated_at']
        # extra_kwargs = {
        #     'thumbnail': {'view_name': 'thumbnail:image-detail'}
        # }
