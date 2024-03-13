from django.db import models

class UserRoles(models.TextChoices):
    ADMIN = "admin"
    USER = "user"

class UserStatus(models.TextChoices):
    ACTIVE = "active"
    INACTIVE = "inactive"