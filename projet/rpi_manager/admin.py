from django.contrib import admin
from rpi_manager import models

admin.site.register(models.WaterSchedule)
admin.site.register(models.LightSchedule)
admin.site.register(models.Rpi)
admin.site.register(models.Ph)
admin.site.register(models.Ec)
