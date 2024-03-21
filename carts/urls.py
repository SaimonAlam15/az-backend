from django.urls import path

from .views import CartListView, CartDetailView, CartItemListView, CartItemDetailView


urlpatterns = [
    path('', CartListView.as_view(), name='cart_list'),
    path('<int:pk>', CartDetailView.as_view(), name='cart_detail'),
    path('items/', CartItemListView.as_view(), name='cart_item_list'),
    path('items/<int:pk>', CartItemDetailView.as_view(), name='cart_item_detail'),
]