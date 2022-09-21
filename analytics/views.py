from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError
from rest_framework import viewsets, mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from analytics.models import CapturedData
from analytics.serializers import CreateCapturedDataSerializer, GetCapturedDataSerializer


class AnalyticsViewSet(mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):
    """
    This is only for when user requested urls' analytics data.
    """
    queryset = CapturedData.objects.all()
    serializer_class = GetCapturedDataSerializer
    http_method_names = ['get', 'delete']


class CollectDataViewSet(viewsets.ModelViewSet):
    """
    This view is intend to be used when JS file collect user data.
    You don't need to use this endpoint **directly**!!!
    """
    authentication_classes = []
    permission_classes = []
    queryset = CapturedData.objects.all()
    serializer_class = CreateCapturedDataSerializer
    http_method_names = ['post']

    def _get_client_ip(self, request: Request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def create(self, request: Request, *args, **kwargs):
        ip_address = self._get_client_ip(request)

        g = GeoIP2()
        try:
            location = g.city(ip_address)

            country = location["country_name"]
            city = location["city"]
            latitude = location["latitude"]
            longitude = location["longitude"]
        except AddressNotFoundError as _:
            country = None
            city = None
            latitude = None
            longitude = None

        c = CapturedData(
            ip_address=ip_address,
            js_reqeust_time_UTC=request.data['js_reqeust_time_UTC'],
            page_loaded_time=request.data['page_loaded_time'],
            page_leave_time=request.data['page_leave_time'],
            referer_url=request.data['referer_url'],
            country=country,
            city=city,
            latitude=latitude,
            longitude=longitude,
        )

        c.save()

        s = CreateCapturedDataSerializer(c)
        return Response(s.data)
