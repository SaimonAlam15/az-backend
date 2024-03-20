from django.db import models

class UserRoles(models.TextChoices):
    ADMIN = "admin"
    CUSTOMER = "customer"


class UserStatus(models.TextChoices):
    ACTIVE = "active"
    INACTIVE = "inactive"


class GenderChoices(models.TextChoices):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
