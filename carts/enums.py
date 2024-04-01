from django.db import models


class CartStatus(models.TextChoices):
    ACTIVE = "active"
    CLOSED = "closed"