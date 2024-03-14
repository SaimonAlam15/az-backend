from django.db import models
from django.contrib.auth.models import AbstractUser

from .enums import UserRoles, UserStatus


class User(AbstractUser):
    class Meta:
        db_table = "users"
        
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    status = models.CharField(choices=UserStatus, max_length=255, default=UserStatus.ACTIVE)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
