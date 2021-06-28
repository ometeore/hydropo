from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from rpi_manager.models import Rpi
from .forms import CreationRpi
from datetime import datetime
import logging
import pytz


LOGGER = logging.getLogger(__name__)


def reset_password(request):
    return render(
        request, "message/error.html", {"issue": "Not available yet. Contact admin."}
    )


def rpi_create(request):
    """we create the rpi with last date at datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
    it is the date for never connected"""
    form = CreationRpi(request.POST)
    if form.is_valid():
        rpi = Rpi.objects.create(name = form.cleaned_data["name"], is_conected = False, last_connect = datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC))
        temp_uid_name = id(rpi)
        while Rpi.objects.filter(uid_name = temp_uid_name).count() != 0:
            temp_uid_name = temp_uid_name + 1
        rpi.uid_name = temp_uid_name
        rpi.save()
        request.user.rpi.add(rpi)
        # request.user.save()
        userlog = request.user
        user_rpi = userlog.rpi.all()
        return render(request, "user/mon_compte.html", {"user_rpi": user_rpi})
    else:
        return render(request, "user/creation_rpi.html", {"form": form})


def rpi_delete(request):

    del_schedule = get_object_or_404(Rpi, pk=request.GET["pk"])
    print(del_schedule.name)
    print(del_schedule)
    del_schedule.delete()
    print(del_schedule)
    return redirect("/user/profil")


def rpi_update(request):

    # Detect wich type of schedule need to be delete
    if request.GET["categori"] == "water":
        del_schedule = get_object_or_404(WaterSchedule, pk=request.GET["pk"])
    else:
        del_schedule = get_object_or_404(LightSchedule, pk=request.GET["pk"])
    del_schedule.delete()
