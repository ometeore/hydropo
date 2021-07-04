from django.shortcuts import render, get_object_or_404
from .forms import PhEc
from rpi_manager.models import Ph, Ec, Rpi
from datetime import datetime
import json


def hydropo_gestion(request):
    ### view of main page and reaction to the different form ###

    userlog = request.user
    user_rpi = userlog.rpi.all()

    # check if the user have a rpi linked to his account
    if not user_rpi:
        err = "No Rpi associated yet!"
        return render(request, "message/error.html", {"issue": err})
    else:
        #creation of the new dict

        context_dict = {
            "rpi": user_rpi,
        }

        if request.method == "GET":
            if request.GET.get("manual", False):
                if request.GET.get("tool", None) is not None:
                    rpi = get_object_or_404(Rpi, name=request.GET["name"])
                    rpi.broadcast_manual(request.GET["tool"])
        ################################################
        # the only form here is the one to change EC and Ph
        # if multiple rpi the id of the one is send on get as rpi_active

        if request.method == "POST":
            phec = PhEc(request.POST)
            if phec.is_valid():

                ph = request.POST.get("ph", False)
                ec = request.POST.get("ec", False)

                if ph:
                    last_ph_set_up = Ph.objects.filter(
                        rpi_id=request.GET["rpi_active"], objectif=True
                    )
                    if int(ph) < 14 and int(ph) > 0:
                        last_ph_set_up.delete()
                        rpi = get_object_or_404(Rpi, pk=request.GET["rpi_active"])
                        new_ph = Ph.objects.create(
                            date=datetime.now(), value=ph, objectif=True, rpi=rpi
                        )
                        new_ph.save()

                if ec:
                    last_ec_set_up = Ec.objects.filter(
                        rpi_id=request.GET["rpi_active"], objectif=True
                    )
                    if int(ec) > 0:
                        last_ec_set_up.delete()
                        rpi = get_object_or_404(Rpi, pk=request.GET["rpi_active"])
                        new_ec = Ec.objects.create(
                            date=datetime.now(), value=ec, objectif=True, rpi=rpi
                        )
                        new_ec.save()

                rpi.broadcast_schedule()

            ####### formulary problem create a page here ######
            else:
                print("manual form aint valid")

        ####### initiate the main screen with clean formularies ######
        else:
            phec = PhEc()

        if request.GET.get("id", False):
            rpi = get_object_or_404(Rpi, pk=request.GET["id"])
            context_dict.update({"active_onglet": rpi.name})

        context_dict.update({"form_phec": phec})

        return render(request, "hydro.html", context=context_dict)
