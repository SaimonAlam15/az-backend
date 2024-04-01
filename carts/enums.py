from django.db import models


class CartStatus(models.TextChoices):
    OPEN = "open"
    CLOSED = "closed"