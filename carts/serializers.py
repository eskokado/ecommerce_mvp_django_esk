from rest_framework import serializers

from carts.models import Cart
from carts_items.models import CartItem
from carts_items.serializers import CartItemSerializer
from django.contrib.auth.models import User

from products.models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'created_at', 'updated_at', 'user', 'items')

    def create(self, validated_data):
        items_data = self.context['request'].data.get('items')
        cart = Cart.objects.create(**validated_data)

        for item_data in items_data:
            product_id = item_data.get('product')
            product = Product.objects.get(id=product_id)
            CartItem.objects.create(
                cart=cart,
                product=product,
                quantity=item_data.get('quantity'),
                unit_price=item_data.get('unit_price')
            )
        return cart

    def update(self, instance, validated_data):
        items_data = self.context['request'].data.get('items')

        if items_data:
            for item_data in items_data:
                if 'id' in item_data:
                    try:
                        cart_item = instance.cartitem_set.get(id=item_data['id'])
                        item_serializer = CartItemSerializer(cart_item, data=item_data, partial=True)
                        if item_serializer.is_valid(raise_exception=True):
                            item_serializer.save()
                    except CartItem.DoesNotExist:
                        pass
                else:
                    # Trata itens novos
                    item_serializer = CartItemSerializer(data=item_data, context={'request': self.context['request']})
                    if item_serializer.is_valid(raise_exception=True):
                        item_serializer.save(cart=instance)

        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        items = instance.cartitem_set.all()
        representation['items'] = CartItemSerializer(items, many=True).data
        return representation
