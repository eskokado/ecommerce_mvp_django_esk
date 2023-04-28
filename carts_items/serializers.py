from rest_framework import serializers

from carts_items.models import CartItem
from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category')


class CartItemSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(read_only=True)
    product = ProductListSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'quantity', 'unit_price', 'product')

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.unit_price = validated_data.get('unit_price', instance.unit_price)

        if instance.quantity == 0:
            instance.delete()
        else:
            instance.save()

        return instance
