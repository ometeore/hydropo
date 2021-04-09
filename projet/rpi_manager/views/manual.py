from django.shortcuts import render
from .forms import PhEc
from rpi_manager.models import WaterSchedule, Ph, Ec, LightSchedule
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def mode(request): 
### view of main page and reaction to the different form ###

    water_schedule = list(WaterSchedule.objects.filter(
        rpi_id = 1
    ))

    light_schedule = list(LightSchedule.objects.filter(
        rpi_id = 1
    ))

    last_ph = Ph.objects.latest('date')
    last_ec = Ec.objects.latest('date')

    phec = PhEc()

    context_dict = {
        "water_schedule" : water_schedule,
        "light_schedule" : light_schedule,
        "last_ph": last_ph,
        "last_ec": last_ec,
        "form_phec":phec,
    }



    if(request.GET["manual"] == "on"):

        temp = request.GET["tool"]
        channel_layer = get_channel_layer()
        
        #reglages_json = json.dumps(context_dict, indent=4, sort_keys=True, default=str)
    
        ####### This part is sending the message to the websocket in group call "group0"
        # type send message is compulsory for the web socket to run
        # i dont know why i shouldn t have to wonder why T T

        async_to_sync(channel_layer.group_send)(
            "group0",
            {
                "type": "send_message",
                "manual": True,
                "message": temp
            }
        )






    else:
        # go to raspbery gestion
        print('boloss')


    return render(request, 'hydro.html', context = context_dict)