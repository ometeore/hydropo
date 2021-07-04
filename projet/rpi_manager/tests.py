from datetime import datetime
from django.test import TestCase
from rpi_manager.models import Rpi, WaterSchedule
from user.models import MyUser
from datetime import datetime, time
import pytz


def do_nothing():
    pass


################################### TEST DU MODELE RPI ####################################


class RpiTestCase(TestCase):
    def setUp(self):
        self.rpi = Rpi.objects.create(
            name="test",
            uid_name="md5_test",
            last_connect=datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
            is_conected=True,
        )

        self.schedule_water1 = WaterSchedule.objects.create(
            begin=time(13, 0, 0), end=time(14, 0, 0), rpi=self.rpi
        )

    def test_compare_time(self):
        self.assertEqual(self.rpi.compare_time("17:0:0", "18:0:0", True), True)
        self.assertEqual(self.rpi.compare_time("11:0:0", "18:0:0", True), False)

    # je dois associer des water_schedule a ma rpi et m'assurer que les messages sont tels qu'ils devraient etre

    async def test_broadcast_schedule(self):
        pass

    def test_broadcast_manual(self):
        pass


    def broadcast_schedule(self):
        message = {}
        message["manual"] = False
        schedule_water_list = [
            [str(elm.begin), str(elm.end)] for elm in self.water.all()
        ]
        message["water"] = schedule_water_list
        schedule_lights_list = [
            [str(elm.begin), str(elm.end)] for elm in self.lights.all()
        ]
        message["lights"] = schedule_lights_list
        objectif_ph = self.ph.filter(objectif=True)
        message["ph"] = objectif_ph[0].value
        objectif_ec = self.ec.filter(objectif=True)
        message["ec"] = objectif_ec[0].value

        ####### This part is sending the message to the websocket in group call "group0"

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            self.uid_name, {"type": "send_message", "message": message}
        )

    def broadcast_manual(self, tool):
        message = {}
        message["manual"] = True
        message["tool"] = tool
        print(message)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            self.uid_name, {"type": "send_message", "message": message}
        )

################################### TEST DES VIEWS RPI ####################################


class TestStatus(TestCase):
    def setUp(self):

        self.user = MyUser.objects.create_user(
            username="jacob", email="jacob@…", password="top_secret"
        )

    def test_home(self):
        ### Test qu'on a bien une reponse en demandant l'accueil ###
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
