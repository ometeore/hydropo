from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path('ws/', consumers.SocketConsumer),      #re_path pour path avec regex (pourrai metre path ici)
]