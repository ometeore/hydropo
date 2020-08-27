from django.shortcuts import render, get_object_or_404
from rpi_manager.models import WaterSchedule, Ph, Rpi
from .forms import AddSchedule, ScheduleFormSet, ManualMode

def add(request):

    if request.method == "POST":
        form = AddSchedule(request.POST)
        if form.is_valid():
            rpi = get_object_or_404(Rpi, pk = 1)
            ph = WaterSchedule.objects.create(begin=request.POST["begin"], end=request.POST["end"], rpi=rpi)
            ph.save()
            schedule = list(WaterSchedule.objects.filter(rpi_id = 1))
            last_ph = Ph.objects.latest('date')
            context_dict = {
                "schedule_list" : schedule,
                "last_ph": last_ph,
            }
            motor_form = ManualMode()
            context_dict.update({"form":motor_form})
            return render(request, 'index.html', context = context_dict)
        
        else:
            errors = form.errors

            return render(request, 'add_schedule.html', {"form": form, "errors": errors})

    else:
        form = AddSchedule()
        return render(request, 'add_schedule.html', {"form": form})



def show(request):
    if request.method == "POST":
        formset = ScheduleFormSet(data=request.POST)

        if formset.is_valid():
            for form in formset:
                print("le formset est valide")

        else:
            print(formset.errors)

    else:
        schedule = WaterSchedule.objects.all()
        formset=ScheduleFormSet(queryset=schedule)
    return render(request, 'schedule.html', {'formset':formset})

def delete(request):

    del_schedule = get_object_or_404(WaterSchedule, pk = request.GET["pk"])
    del_schedule.delete()
    schedule = list(WaterSchedule.objects.filter(rpi_id = 1))
    last_ph = Ph.objects.latest('date')
    context_dict = {
        "schedule_list" : schedule,
        "last_ph": last_ph,
    }
    motor_form = ManualMode()
    context_dict.update({"form":motor_form})
    return render(request, 'index.html', context = context_dict)

