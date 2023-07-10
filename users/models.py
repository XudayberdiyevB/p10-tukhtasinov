from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    password = models.CharField()

    def __str__(self):
        return self.username
