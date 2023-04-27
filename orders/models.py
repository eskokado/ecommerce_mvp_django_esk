from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    shipping_address = models.TextField()
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} - User {self.user.username}"
