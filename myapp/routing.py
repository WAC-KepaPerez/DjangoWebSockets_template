from django.urls import re_path
from .consumers import *

websocket_urlpatterns = [
    re_path(r'^ws/somepath/$', EchoConsumer.as_asgi()),
    re_path(r'^ws/contar/$', ContarConsumer.as_asgi()),
]