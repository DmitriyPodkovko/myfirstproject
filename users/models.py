from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    avatar = models.ImageField(blank=True, null=True)

    def __str__(self):
        return "@{}".format(self.username)
