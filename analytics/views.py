from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from analytics.models import CapturedData
from analytics.serializers import CreateCapturedDataSerializer, GetCapturedDataSerializer


class AnalyticsViewSet(mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):
    """
    This is only for when user requested urls' analytics data.
    """
    queryset = CapturedData
    serializer_class = GetCapturedDataSerializer
    http_method_names = ['get', 'delete']


class CollectDataViewSet(viewsets.ModelViewSet):
    """
    This view is intend to be used when JS file collect user data.
    """
    queryset = CapturedData
    serializer_class = CreateCapturedDataSerializer
    http_method_names = ['post']
