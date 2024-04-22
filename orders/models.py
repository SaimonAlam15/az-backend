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
    address = models.ForeignKey(
        'users.AddressBook', null=True, on_delete=models.SET_NULL
    )

    class Meta:
        db_table = "orders"

    def save(self, *args, **kwargs):
        if self.status not in [
            OrderStatus.PENDING, OrderStatus.PROCESSING,
            OrderStatus.ON_HOLD, OrderStatus.SHIPPED
            ]:
            self.cart.status = 'closed'
            self.cart.save()
        super().save(*args, **kwargs)
