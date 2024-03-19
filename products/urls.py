from django.urls import path

from .views import ProductListView, ProductDetailView, ProductImageListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('images/', ProductImageListView.as_view(), name='product_image_list'),
]