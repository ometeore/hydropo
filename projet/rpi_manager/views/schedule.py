from django.shortcuts import render, get_object_or_404
from rpi_manager.models import WaterSchedule, Ph, Rpi, Ec, LightSchedule
from .forms import AddSchedule, ScheduleFormSet, ManualMode, PhEc

def add(request):
    rpi_active = request.GET["rpi_active"]

    if request.method == "POST":
        form = AddSchedule(request.POST)
        if form.is_valid():
            # metre la rpi de l'utilisateur
            rpi = get_object_or_404(Rpi, pk = request.GET["rpi_active"])

            if(request.GET["categori"] == "water"):
                if rpi.compare_time(request.POST["begin"], request.POST["end"], True):
                    schedule = WaterSchedule.objects.create(begin=request.POST["begin"], end=request.POST["end"], rpi=rpi)
                    schedule.save()
                    rpi.broadcast_schedule()
                else:
                    #### page pour dire que le schedule entre en conflit avec les previous schedule
                    print("schedule non valide")

            if(request.GET["categori"] == "lights"):
                if rpi.compare_time(request.POST["begin"], request.POST["end"], False):
                    schedule = LightSchedule.objects.create(begin=request.POST["begin"], end=request.POST["end"], rpi=rpi)
                    schedule.save()
                    rpi.broadcast_schedule()
                else:
                    #### page pour dire que le schedule entre en conflit avec les previous schedule
                    print("schedule non valide")

            userlog = request.user
            user_rpi = userlog.rpi.all()
            phec = PhEc()

            context_dict = {
                "rpi" : user_rpi,
                "form_phec" : phec
            }

            return render(request, 'hydro.html', context = context_dict)
        
        else:
            errors = form.errors

            return render(request, 'schedule/add_schedule.html', {"form": form, "errors": errors})

    else:
        form = AddSchedule()
        return render(request, 'schedule/add_schedule.html', {"form": form, "categori": request.GET["categori"], "rpi_active": request.GET["rpi_active"]})



def delete(request):

    rpi = get_object_or_404(Rpi, pk = request.GET["rpi"])


    #Detect wich type of schedule need to be delete
    if(request.GET["categori"] == "water"):
        del_schedule = get_object_or_404(WaterSchedule, pk = request.GET["pk"])
    else:
        del_schedule = get_object_or_404(LightSchedule, pk = request.GET["pk"])
    del_schedule.delete()
    rpi.broadcast_schedule()

    userlog = request.user
    user_rpi = userlog.rpi.all()

    context_dict = {
        "rpi" : user_rpi,
    }

    motor_form = ManualMode()
    context_dict.update({"form":motor_form})
    return render(request, 'hydro.html', context = context_dict)

