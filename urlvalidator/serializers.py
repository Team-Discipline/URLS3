from rest_framework import serializers
from urlvalidator.models import URLModel


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLModel
        fields = ['scheme', 'netloc', 'path', 'hostname', 'port', 'params', 'query', 'fragment']
