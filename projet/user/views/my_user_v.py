from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from user.models import MyUser
from .forms import Connexion, Creation


def connexion(request):
    if request.method == "POST":

        # create a form instance and populate it with data from the request:
        form = Connexion(request.POST)
        # check whether it's valid:
        if form.is_valid():
            identifiant = form.cleaned_data["identifiant"]
            mdp = form.cleaned_data["password"]
            user = authenticate(username=identifiant, password=mdp)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return render(
                    request, "user/connexion.html", {"form": form, "invalid": True}
                )

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

        # Check if user exists with email
        try:
            alt_user = MyUser.objects.get(email=form.cleaned_data["email"])
            return render(request, "message/error.html", {"issue": "Mail already use"})
        except Exception as e:
            print("[LOG] No issue with new user setup" + str(e))

        if form.cleaned_data["confirm_password"] == form.cleaned_data["password"]:
            user = MyUser.objects.create_user(form.cleaned_data["Username"])
            user.set_password(form.cleaned_data["password"])
            user.last_name = form.cleaned_data["last_name"]
            user.first_name = form.cleaned_data["first_name"]
            user.email = form.cleaned_data["email"]
            user.save()
            new_user = authenticate(
                username=form.cleaned_data["Username"],
                password=form.cleaned_data["confirm_password"],
            )
            login(request, new_user)
            return render(request, "home.html")
        else:
            render(
                request,
                "user/creation.html",
                {"form": form, "password_not_identic": True},
            )
    return render(request, "user/creation.html", {"form": form})


def deconnexion(request):
    logout(request)
    return redirect("/")
