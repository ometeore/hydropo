from django.db import models
from django import forms
from datetime import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class Rpi(models.Model):
    name = models.CharField(max_length=200)
    md5_name = models.CharField(max_length=200)
    last_connect = models.DateTimeField()

#plutot que de comparer des str sources de bugs
# import datetime
# regler le passage a minuit aussi
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
    def compare_time(self, begin_test, end_test, cat):
        if cat:
            schedule = self.water.all()
        else:
            schedule = self.lights.all()

        for times in schedule:
            if (begin_test > str(times.begin) and begin_test < str(times.end)):
                return False
            if (end_test > str(times.begin) and end_test < str(times.end)):
                return False
            if (begin_test < str(times.begin) and end_test > str(times.end)):
                return False

        return True 
    

    def broadcast(self):
        message = {}
        message["manual"] = False
        schedule_water_list = [[str(elm.begin), str(elm.end)] for elm in self.water.all()]
        message["water"] = schedule_water_list
        schedule_lights_list = [[str(elm.begin), str(elm.end)] for elm in self.lights.all()]
        message["lights"] = schedule_lights_list
        objectif_ph = self.ph.filter(objectif=True)
        message["ph"] = objectif_ph[0].value
        objectif_ec = self.ec.filter(objectif=True)
        message["ec"] = objectif_ec[0].value
    
        ####### This part is sending the message to the websocket in group call "group0"

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            md5_name,
            {
                "type": "send_message",
                "message": message
            }
        )

    def manual(self, options):
        message = {}
        message["manual"] = True
        message["option"] = options
        
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            md5_name,
            {
                "type": "send_message",
                "message": message
            }
        )


class WaterSchedule(models.Model):
    begin = models.TimeField()
    end = models.TimeField()
    rpi = models.ForeignKey(Rpi, on_delete=models.CASCADE, related_name = "water")

class LightSchedule(models.Model):
    begin = models.TimeField()
    end = models.TimeField()
    rpi = models.ForeignKey(Rpi, on_delete=models.CASCADE, related_name = "lights")

class Ph(models.Model):
    date = models.DateTimeField()
    value = models.FloatField()
    objectif = models.BooleanField()
    rpi = models.ForeignKey(Rpi, on_delete=models.CASCADE, related_name = "ph")

class Ec(models.Model):
    date = models.DateTimeField()
    value = models.IntegerField()
    objectif = models.BooleanField()
    rpi = models.ForeignKey(Rpi, on_delete=models.CASCADE, related_name = "ec")