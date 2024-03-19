from django.db import models

from azshop.models import BaseModel
from .enums import ProductStatus, ProductCategories, ProductTags

# Create your models here.
class Product(BaseModel):
    class Meta:
        db_table = "products"
        
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(null=True, blank=True, default=None)
    description = models.TextField()
    ingredients = models.TextField()
    category = models.CharField(choices=ProductCategories.choices, max_length=255)
    tags = models.CharField(
        choices=ProductTags.choices, 
        max_length=255, default=ProductTags.NEW
    )
    status = models.CharField(
        choices=ProductStatus.choices, 
        max_length=255, default=ProductStatus.ACTIVE
    )

    def __str__(self):
        return str(self.name)


class ProductImage(BaseModel):
    class Meta:
        db_table = "product_images"

    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    url = models.ImageField(upload_to="photos/")
    rank = models.IntegerField(default=1)

    def __str__(self):
        return str(self.name)
