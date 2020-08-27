from django.shortcuts import render
from .forms import ManualMode, TerminalControl
from rpi_manager.models import WaterSchedule, Ph
from datetime import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def index(request): 


    ###### page context
    schedule = list(WaterSchedule.objects.filter(
        rpi_id = 1
    ))
    last_ph = Ph.objects.latest('date')
    context_dict = {
        "schedule_list" : schedule,
        "last_ph": last_ph,
    }

    ###### prepare to send with websocket
    temp = ""
    for elm in context_dict["schedule_list"]:
        temp += elm.begin.strftime("%H:%M") + " , " + elm.end.strftime("%H:%M") + " | "
    good_ph = list(Ph.objects.filter(id=1))
    temp += "ph : " + str(good_ph[0].value)
    print(temp)



    if request.method == "POST":
        motor_form = ManualMode(request.POST)
        if motor_form.is_valid():
            print("form is valid")
            channel_layer = get_channel_layer()
            
            ####### This part is sending the message to the websocket in group call "group0"
            async_to_sync(channel_layer.group_send)(
                "group0",
                {
                    "type": "send_message",
                    "message": temp
                }
            )
            #######
        else:
            print("manual form aint valid")

    else:
        motor_form = ManualMode()

    context_dict.update({"form":motor_form})
    return render(request, 'index.html', context = context_dict)
