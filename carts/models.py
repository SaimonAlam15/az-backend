from django.db import models

from azshop.models import BaseModel
from .enums import CartStatus


class Cart(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    status = models.CharField(choices=CartStatus.choices, max_length=16, default=CartStatus.OPEN)

    class Meta:
        db_table = "carts"


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = "cart_items"
