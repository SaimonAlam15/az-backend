from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Order
from .serializers import OrderListSerializer, OrderDetailSerializer


class OrderListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all().prefetch_related("cart__items")
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
