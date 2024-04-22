from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Order
from .serializers import OrderListSerializer, OrderDetailSerializer


class OrderListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all().prefetch_related("cart__items")
    serializer_class = OrderDetailSerializer
