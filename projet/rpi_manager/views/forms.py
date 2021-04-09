from django.forms import ModelForm, Form
from rpi_manager.models import WaterSchedule
from django.forms import modelformset_factory, ModelForm
from django import forms


class PhEc(Form):
    ph = forms.FloatField(min_value=0, max_value=14, required=False, widget=forms.TextInput)
    ec = forms.IntegerField(min_value=0, required=False, widget=forms.TextInput)


class ManualMode(Form):
    water_pump = forms.BooleanField(required=False )
    solenoid_valve_ph = forms.BooleanField(required=False )
    solenoid_valve_conduct = forms.BooleanField(required=False )
    begin = forms.TimeField(required=False )
    end = forms.TimeField(required=False )


class AddSchedule(Form):
    begin = forms.TimeField()
    end = forms.TimeField()
    

class SeeSchedule(ModelForm):
    #C'ets ici que je peux désactiver l'input de name

    class Meta:
        model = WaterSchedule
        exclude = ()

        help_texts = {
            'nom': ('Some useful help text.'),
        }
        error_messages = {
            'nom': {
                'max_length': ("This writer's name is too long."),
            },
        }

ScheduleFormSet = modelformset_factory(WaterSchedule, form=SeeSchedule)
