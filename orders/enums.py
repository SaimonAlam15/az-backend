from django.db import models

class OrderStatus(models.TextChoices):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"
    FAILED = "failed"
    ON_HOLD = "on_hold"
    SHIPPED = "shipped"
    RETURNED = "returned"
    EXCHANGED = "exchanged"


class PaymentMethod(models.TextChoices):
    COD = "cod"
    CARD = "card"
    PAYPAL = "paypal"
    OTHER = "other"

