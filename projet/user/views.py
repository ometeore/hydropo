from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from user.models import MyUser
from rpi_manager.models import Rpi
from .forms import Connexion, Creation, CreationRpi
import logging

LOGGER=logging.getLogger(__name__)


def connexion(request):
    if request.method == "POST":

        # create a form instance and populate it with data from the request:
        form = Connexion(request.POST)
        # check whether it's valid:
        if form.is_valid():
            identifiant = form.cleaned_data["identifiant"]
            mdp = form.cleaned_data["password"]
            user = authenticate(username=identifiant, password=mdp)

            #LOGGER.info("le mot de passe" + mdp)
            #LOGGER.warn("le mot de passe" + mdp)
            
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return render(request, "user/connexion.html", {"form": form, "invalid": True})

    else:
        form = Connexion()
        return render(request, "user/connexion.html", {"form": form})
 

def mon_compte(request):
    userlog = request.user
    user_rpi = userlog.rpi.all()
    return render(request, "user/mon_compte.html", {"user_rpi": user_rpi})

def create(request):
    form = Creation(request.POST)
    if form.is_valid():
        if form.cleaned_data["confirm_password"] == form.cleaned_data["password"]:
            user = MyUser.objects.create_user(form.cleaned_data["Username"])
            user.set_password(form.cleaned_data["password"])
            user.last_name = form.cleaned_data["last_name"]
            user.first_name = form.cleaned_data["first_name"]
            user.email = form.cleaned_data["email"]
            user.save()
            return render(request, "home.html")
        else:
            render(request, "user/creation.html", {"form": form})
    return render(request, "user/creation.html", {"form": form})


def deconnexion(request):
    logout(request)
    return redirect("/")





def rpi_create(request):
    form = CreationRpi(request.POST)
    if form.is_valid():
        rpi = Rpi.objects.create()
        print("rpicreate")
        rpi.name = form.cleaned_data["name"]
        rpi.save()
        print("rpi save")
        request.user.rpi.add(rpi)
        print("rpi add to user")
        #request.user.save()
        userlog = request.user
        user_rpi = userlog.rpi.all()
        return render(request, "user/mon_compte.html", {"user_rpi": user_rpi})
    else:
        print("ok")
        return render(request, "user/creation_rpi.html", {"form": form})

def rpi_delete(request):

    del_schedule = get_object_or_404(Rpi, pk = request.GET["pk"])
    print(del_schedule.name)
    print(del_schedule)
    del_schedule.delete()
    print(del_schedule)
    return redirect('/user/profil')

def rpi_update(request):

    #Detect wich type of schedule need to be delete
    if(request.GET["categori"] == "water"):
        del_schedule = get_object_or_404(WaterSchedule, pk = request.GET["pk"])
    else:
        del_schedule = get_object_or_404(LightSchedule, pk = request.GET["pk"])
    del_schedule.delete()

