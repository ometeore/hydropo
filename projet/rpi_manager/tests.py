from datetime import datetime
from django.test import TestCase
from rpi_manager.models import Rpi, WaterSchedule
from datetime import datetime, time

class RpiTestCase(TestCase):
    def setUp(self):
        self.rpi = Rpi.objects.create(name="test", md5_name="md5_test", last_connect=datetime(2020,1,1,1,1,1), is_conected = True)

        self.schedule_water1 = WaterSchedule.objects.create(begin=time(13,0,0), end=time(14,0,0), rpi=self.rpi)

    def test_compare_time(self):
        self.assertEqual(self.rpi.compare_time("17:0:0", "18:0:0", True ), True)
        self.assertEqual(self.rpi.compare_time("11:0:0", "18:0:0", True ), False)

    def test_broadcast_schedule(self):
        pass

    def test_broadcast_manual(self):
        pass
