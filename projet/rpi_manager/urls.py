from django.urls import path
from rpi_manager.views import schedule

app_name = "rpi"

urlpatterns = [
    path("add_schedule", schedule.add, name="add_schedule"),
    path("schedule", schedule.show, name="schedule"),
    path("delete", schedule.delete, name="delete_schedule"),
]