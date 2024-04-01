from django.db import models

from azshop.models import BaseModel
from carts.models import Cart
from .enums import OrderStatus, PaymentMethod


class Order(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    payment_method = models.CharField(
        choices=PaymentMethod.choices, max_length=255,
        default=PaymentMethod.COD
    )
    status = models.CharField(
        choices=OrderStatus.choices, max_length=255,
        default=OrderStatus.PENDING
    )

    class Meta:
        db_table = "orders"
