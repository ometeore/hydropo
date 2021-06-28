import json
from datetime import datetime
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from rpi_manager.models import Rpi, Ec, Ph


# The solution is in database async to sync in channels.db
class SocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]

        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
        await self.database_conect_rpi()
        print("New conection; UID: {}".format(self.room_name))

    async def disconnect(self, close_code):
        print(self.room_name)
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
        await self.database_disconect_rpi()
        print("the rpi {} is disconectd from server".format(self.room_name))

    # Receive message from WebSocket
    async def receive(self, text_data):
        rpi_message = json.loads(text_data)
        print(type(rpi_message))
        try:
            await self.database_save_rpi_new_data(rpi_message)
        except Exception as err:
            print(err)

    async def send_message(self, message):
        print("message a envoyer: {}".format(message))
        message_to_send = {"message": message}
        j = json.dumps(message_to_send)
        await self.send(j)

    ################ FUNCTIONS TO WORK WITH SYNC DB
    @database_sync_to_async
    def database_disconect_rpi(self):
        Rpi.objects.filter(uid_name=self.room_name).update(is_conected=False)

    @database_sync_to_async
    def database_conect_rpi(self):
        time_now = datetime.now()
        try:
            Rpi.objects.filter(uid_name=self.room_name).update(
                is_conected=True, last_connect=time_now
            )
        except Exception as err:
            print(err)

    @database_sync_to_async
    def database_save_rpi_new_data(self, rpi_message):
        my_rpi = Rpi.objects.get(uid_name=self.room_name)
        new_ec = Ec.objects.create(
            date=datetime.now(), value=rpi_message["ec"], objectif=False, rpi=my_rpi
        )
        new_ec.save()
        new_ph = Ph.objects.create(
            date = datetime.now(), value = rpi_message['ph'], objectif = False, rpi = my_rpi
        )
        new_ph.save()
