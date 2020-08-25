import json
import channels
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

class SocketConsumer(AsyncWebsocketConsumer):


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
        print("a recu un message est rentré dans receive du consumer")
        # Send message to room group
        await self.channel_layer.group_send(
            
            "group0",
            {
                'type': 'chat_message',
                'message': text_data
            }
        )

    async def send_message(self, message):
        print(message)
        # Send message to WebSocket
        #self.send(message) #'SocketConsumer' object has no attribute 'base_send' surement (async or sync pb)
        await self.send(message['message'])
        print("ca plante avant")