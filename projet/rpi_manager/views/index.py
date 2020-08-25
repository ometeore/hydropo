from django.shortcuts import render
from .forms import ManualMode, TerminalControl
from rpi_manager.models import WaterSchedule
from datetime import datetime


def index(request):

    if request.method == "POST":
        motor_form = ManualMode(request.POST)
        if motor_form.is_valid():
            print("form is valid")
        else:
            print("manual form aint valid")

    else:
        motor_form = ManualMode()
        schedule = list(WaterSchedule.objects.filter(
            rpi_id = 1
        ))
        context = {
            "schedule_list" : schedule,
        }
        print(context)
        return render(request, 'index.html', {'form':motor_form}, context)

"""
        context = []
        if(schedule == []):
            print("Schedule is empty")
        else:
            for e in schedule:
                temp = []
                temp.append(e.begin.strftime("%H:%M"))
                temp.append(e.end.strftime("%H:%M"))
                context.append(temp)
"""

 

 