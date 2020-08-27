from django.db import models
from django import forms


class Rpi(models.Model):
    name = models.CharField(max_length=200)


class WaterSchedule(models.Model):
    begin = models.TimeField()
    end = models.TimeField()
    rpi = models.ForeignKey(Rpi, on_delete=models.CASCADE)

class Ph(models.Model):
    date = models.DateTimeField()
    value = models.FloatField()
    rpi = models.ForeignKey(Rpi, on_delete=models.CASCADE)
