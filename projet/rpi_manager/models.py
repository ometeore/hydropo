from django.db import models
from django.forms import ModelForm, Form, modelformset_factory
from django import forms


class Rpi(models.Model):
    name = models.CharField(max_length=200)



class WaterSchedule(models.Model):

    begin = models.TimeField()#widget=forms.TimeInput(format='%H:%M'))
    end = models.TimeField()#widget=forms.TimeInput(format='%H:%M'))
    rpi = models.ForeignKey(Rpi, on_delete=models.CASCADE)
