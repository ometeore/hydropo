from os.environ import setdefault
from channels.asgi import get_channel_layer
from channels.routing import ProtocolTypeRouter, URLRouter
from channels


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hydropo.settings')

# application = ProtocolTypeRouter({
# 	"http": get_asgi_application()
# 	"websocket"
# 	})
channel_layer = channels.asgi.get_channel_layer()


# import os
# import django
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# from django.conf.urls import url

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hydropo.settings')
# django_asgi_app = get_asgi_application()

# ######### why

# #django.setup()

# from channels.auth import AuthMiddlewareStack
# from socket_connection.consumers import SocketConsumer
# #from channels.layers import get_channel_layer


# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     "websocket": AuthMiddlewareStack(
#        URLRouter([
#             url("ws/", SocketConsumer.as_asgi()),
#         ])
#     ),
# })

# #channel_layer = get_channel_layer()
