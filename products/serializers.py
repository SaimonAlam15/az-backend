from rest_framework import serializers

from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'name', 'url', 'rank']
        extra_kwargs = {
            'product': {'write_only': True},
        }


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'stock', 
            'category', 'tags', 'status', 'images'
        ]
    
    def get_images(self, obj):
        return ProductImageSerializer(
            obj.images.all().order_by('rank'), many=True).data