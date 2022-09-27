from rest_framework import serializers

from access_key.models import UserAccessKey


class CreateUserAccessKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccessKey
        exclude = ['id', ]


class GetUserAccessKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccessKey
        fields = '__all__'
