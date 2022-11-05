from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/ad_page/(?P<hashed_value>\w+)/$", consumers.AdPageConsumer.as_asgi()),
]
