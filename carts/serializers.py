from rest_framework import serializers

from carts.models import Cart
from carts_items.serializers import CartItemSerializer


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = "__all__"
