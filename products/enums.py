from django.db import models

class ProductTags(models.TextChoices):
    NEW = "new"
    HOT = "hot"

class ProductStatus(models.TextChoices):
    ACTIVE = "active"
    INACTIVE = "inactive"

class ProductCategories(models.TextChoices):
    ELECTRONICS = "electronics"
    FASHION = "fashion"
    HOME = "home"
    BEAUTY = "beauty"
    SPORTS = "sports"
    TOYS = "toys"
    FOOD = "food"
    BOOKS = "books"
    OTHERS = "others"