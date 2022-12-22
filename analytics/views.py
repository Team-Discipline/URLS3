from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError
from rest_framework import viewsets, generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from S3.models import S3
from analytics.models import CapturedData, UniqueVisitor
from analytics.serializers import CreateCapturedDataSerializer, GetCapturedDataSerializer, UniqueVisitorSerializer


class AnalyticsViewSet(generics.ListAPIView):
    """
    This is only for when user requested urls' analytics data.
    """
    queryset = CapturedData.objects.all()
    serializer_class = GetCapturedDataSerializer
    http_method_names = ['get']
    lookup_field = 's3_id'  # That doesn't work! I don't even know...

    def get_queryset(self):
        return CapturedData.objects.filter(s3_id=self.kwargs['s3_id'])


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
        """
        s3필드에 s3_url를 입력 하면 됩니다. 제대로 된 url 주소를 입력 받지 못했을 때 400 오류가 납니다.
        response에 있는 `id`값이 `CapturedData`의 id값 입니다.
        이 값을 websocket 연결 후 `captured_data`에 넣어주세요.
        url은 `ws://127.0.0.1:8000/ws/ad_page/<str:hashed_value>/`
        body는 `{ captured_data": id }`
        """
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

        if request.data.get('s3', None) is None:
            return Response(data={'message': 'invalid data in \"s3\"'}, status=status.HTTP_400_BAD_REQUEST)

        s3: str = request.data['s3']

        try:
            s3: S3 = S3.objects.get(s3_url=s3)
        except S3.DoesNotExist:
            return Response(data={'message': '입력받은 url로 s3를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

        c = CapturedData(
            s3=s3,
            ip_address=ip_address,
            js_request_time_UTC=request.data.get('js_request_time_UTC', None),
            page_loaded_time=request.data.get('page_loaded_time', None),
            page_leave_time=request.data.get('page_leave_time', None),
            referer_url=request.data.get('referer_url', None),
            country=country,
            city=city,
            latitude=latitude,
            longitude=longitude,
        )

        c.save()

        s = GetCapturedDataSerializer(c, context={'request': request})
        return Response(s.data)


class UniqueVisitorsViewSet(generics.ListAPIView):
    queryset = UniqueVisitor.objects.all()
    serializer_class = UniqueVisitorSerializer
    http_method_names = ['get']
    lookup_field = 's3_id'
