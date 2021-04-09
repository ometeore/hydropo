from django.urls import path
from rpi_manager.views import schedule, home, gestion, manual

app_name = "rpi"

urlpatterns = [
    path("gestion", gestion.hydropo_gestion, name="gestion"),
    path("manual", manual.mode, name="manual"),
    path("add_schedule", schedule.add, name="add_schedule"),
    path("delete", schedule.delete, name="delete_schedule"),
]