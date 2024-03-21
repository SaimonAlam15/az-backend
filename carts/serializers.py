from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Cart, CartItem


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(ModelSerializer):
    items = SerializerMethodField()
    class Meta:
        model = Cart
        fields = "__all__"

    def get_items(self, obj):
        items_list = []
        items = obj.items.all()
        for item in items:
            items_list.append({
                "product_id": item.product.id,
                "quantity": item.quantity
            })
        return items_list