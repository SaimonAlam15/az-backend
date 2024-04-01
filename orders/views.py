from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Order
from .serializers import OrderSerializer


class OrderListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all().prefetch_related("cart__items")
    serializer_class = OrderSerializer
