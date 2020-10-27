from django.shortcuts import render
from .forms import ManualMode, TerminalControl
from rpi_manager.models import WaterSchedule, Ph
from datetime import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

def index(request): 
### view of main page and reaction to the different form ###

    schedule = list(WaterSchedule.objects.filter(
        rpi_id = 1
    ))
    temp = []
    for i in range(len(schedule)):
        temp = [schedule[i].begin, schedule[i].end]
        schedule[i] = temp
        temp = []

    last_ph = int(Ph.objects.latest('date').value)

    context_dict = {
        "schedule_list" : schedule,
        "last_ph": last_ph,
    }
    #reglages_json = json.dumps(context_dict, indent = 4)
    reglages_json = json.dumps(context_dict, indent=4, sort_keys=True, default=str)
    #good_ph = list(Ph.objects.filter(id=1))
    #temp += "ph : " + str(good_ph[0].value)
    print(reglages_json)



    if request.method == "POST":
        motor_form = ManualMode(request.POST)
        if motor_form.is_valid():
            channel_layer = get_channel_layer()
            
            ####### This part is sending the message to the websocket in group call "group0"
            async_to_sync(channel_layer.group_send)(
                "group0",
                {
                    "type": "send_message",
                    "message": reglages_json
                }
            )
            #######
        else:
            print("manual form aint valid")

    else:
        motor_form = ManualMode()

    context_dict.update({"form":motor_form})
    return render(request, 'index.html', context = context_dict)
