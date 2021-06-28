from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    rpi = models.ManyToManyField("rpi_manager.Rpi", blank=True)  # int(11) NOT NULL,

    def __str__(self):
        return self.email
