from rest_framework import serializers

from carts.serializers import UserSerializer
from orders.models import Order
from orders_items.models import OrderItem
from orders_items.serializers import OrderItemSerializer
from products.models import Product


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'created_at', 'updated_at', 'user', 'items')

    def create(self, validated_data):
        items_data = self.context['request'].data.get('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            product_id = item_data.get('product')
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item_data.get('quantity'),
                unit_price=item_data.get('unit_price')
            )

        return order

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        items = instance.orderitem_set.all()
        representation['items'] = OrderItemSerializer(items, many=True).data
        return representation
