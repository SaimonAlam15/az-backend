from django.db import models

from azshop.models import BaseModel
from .enums import GenderChoices


class Customers(BaseModel):
    class Meta:
        db_table = "customers"

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    gender = models.CharField(choices=GenderChoices, max_length=10)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class AddressBook(BaseModel):
    class Meta:
        db_table = "address_book"

    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name="addresses")
    address = models.TextField()
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=10, null=True, blank=True, default=None)
    label = models.CharField(max_length=255)

    def __str__(self):
        return str(self.customer.name + ' - ' + self.label)
