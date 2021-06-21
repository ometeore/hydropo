from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path('ws/(?P<room_name>\w+)/$', consumers.SocketConsumer),      #re_path pour path avec regex (pourrai metre path ici)
]