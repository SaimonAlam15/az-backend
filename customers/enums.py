from django.db import models

class GenderChoices(models.TextChoices):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
