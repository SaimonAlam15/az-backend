from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartListView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get("user_id")
        product = request.data.get("product")
        quantity = request.data.get("quantity")
        cart = Cart.objects.filter(
            user=user_id, status="active").order_by("-created_at").first()
        if not cart:
            cart = Cart.objects.create(user_id=user_id)
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        data = {"cart": cart.id, "product": product, "quantity": quantity}
        serializer = None
        if cart_item:
            data["quantity"] += cart_item.quantity
            serializer = CartItemSerializer(cart_item, data=data, partial=True)
        else:
            serializer = CartItemSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all().prefetch_related("items")
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CartItemListView(ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CartItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
