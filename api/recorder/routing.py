from django.urls import re_path
from . import consumers

ws_urlpatterns = [
    re_path(r'ws/stream/$', consumers.wsconsumer.as_asgi()),
]
