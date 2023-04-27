from django.db import models

from carts.models import Cart
from products.models import Product


class CartItem(models.Model):
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart {self.cart.id} - Item {self.id}"
