from rest_framework import serializers

from carts_items.serializers import ProductListSerializer
from orders_items.models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    product = ProductListSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'quantity', 'unit_price', 'product')

