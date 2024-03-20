from django.db import models
from django.contrib.auth.models import AbstractUser

from azshop.models import BaseModel
from .enums import UserRoles, UserStatus, GenderChoices


class User(AbstractUser):
    class Meta:
        db_table = "users"
        
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    gender = models.CharField(choices=GenderChoices, max_length=10, null=True, blank=True)
    status = models.CharField(choices=UserStatus, max_length=255, default=UserStatus.ACTIVE)
    role = models.CharField(choices=UserRoles, max_length=255, default=UserRoles.CUSTOMER)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"


class AddressBook(BaseModel):
    class Meta:
        db_table = "address_book"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    address = models.TextField()
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=10, null=True, blank=True, default=None)
    label = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.__str__()} - {self.label}"

