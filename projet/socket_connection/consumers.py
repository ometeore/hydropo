import json
import channels
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from rpi_manager.models import Rpi

######### ici import rpi dans connect is connect 

######### pour is connect on doit attendre dans tous les salons
# for chat_name in chats:
#     await channel_layer.group_send(
#         chat_name,
#         {"type": "chat.system_message", "text": announcement_text},
#     )

class SocketConsumer(AsyncWebsocketConsumer):
    # for rpi in Rpi.objects.all():
    #     client_list.append()
    async def connect(self):
        
        await self.channel_layer.group_add(
            "group0",
            self.channel_name
        )
        await self.accept()
        print("connection accepted")


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "group0",
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
