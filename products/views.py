from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import ProductSerializer, ProductImageSerializer
from .models import Product, ProductImage


class ProductListView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().prefetch_related('images')


class ProductImageListView(ListCreateAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()