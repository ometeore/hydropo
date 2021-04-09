from django.urls import path
from user import views

app_name = "user"


urlpatterns = [
    path("", views.connexion, name="connexion"),
    path("profil", views.mon_compte, name="profil_user"),
    path("create", views.create, name="inscription"),
    path("deconnexion", views.deconnexion, name="deconnexion"),
    path("rpi_create", views.rpi_create, name="add_rpi"),
    path("rpi_update", views.rpi_update, name="rpi_update"),
    path("rpi_delete", views.rpi_delete, name="rpi_delete"),
]
 