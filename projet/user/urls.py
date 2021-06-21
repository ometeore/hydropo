from django.urls import path
from user.views import my_user_v, rpi_views

app_name = "user"


urlpatterns = [
    path("", my_user_v.connexion, name="connexion"),
    path("profil", my_user_v.mon_compte, name="profil_user"),
    path("create", my_user_v.create, name="inscription"),
    path("deconnexion", my_user_v.deconnexion, name="deconnexion"),
    #concern the RPI
    path("rpi_create", rpi_views.rpi_create, name="add_rpi"),
    path("rpi_update", rpi_views.rpi_update, name="rpi_update"),
    path("rpi_delete", rpi_views.rpi_delete, name="rpi_delete"),
    #YET TO DO
    path("reset_password", rpi_views.reset_password, name="password_reset"),
]
 