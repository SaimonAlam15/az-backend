from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Cart, CartItem


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(ModelSerializer):
    items = SerializerMethodField()
    subtotal = SerializerMethodField()
    class Meta:
        model = Cart
        fields = "__all__"

    def get_items(self, obj):
        items_list = []
        items = obj.items.all()
        for item in items:
            items_list.append({
                "id": item.id,
                "product_id": item.product.id,
                "quantity": item.quantity
            })
        return items_list

    def get_subtotal(self, obj):
        items = obj.items.all()
        total = 0
        for item in items:
            total += item.product.price * item.quantity
        return total