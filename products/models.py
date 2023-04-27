from django.db import models

from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url_image = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
