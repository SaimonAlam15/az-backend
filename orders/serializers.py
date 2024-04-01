from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Order

class OrderSerializer(ModelSerializer):
    items = SerializerMethodField()
    subtotal = SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"

    def get_items(self, obj):
        items_list = []
        items = obj.cart.items.all()
        for item in items:
            items_list.append({
                "name": item.product.name,
                "price": item.product.price,
                "quantity": item.quantity
            })
        return items_list
    
    def get_subtotal(self, obj):
        items = obj.cart.items.all()
        total = 0
        for item in items:
            total += item.product.price * item.quantity
        return total