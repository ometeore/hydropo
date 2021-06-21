import json
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from rpi_manager.models import Rpi





@database_sync_to_async
def conect_rpi(room_name):
    rpi = Rpi.objects.filter(uid_name=room_name)
    rpi.is_connected = True
    print(rpi.is_conected)
    return "boloss"

# The solution is in database async to sync in channels.db
class SocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()
        print(conect_rpi(self.room_name))
        print("New conection; UID: {}".format(self.room_name))




    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print("is diconected from the server")

    # Receive message from WebSocket
    async def receive(self, text_data):
        print(text_data)


    async def send_message(self, message):
        print("message a envoyer:")
        print(message)
        message_to_send = {
            "message": message
        }
        j = json.dumps(message_to_send)
        await self.send(j)
