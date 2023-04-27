from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url_image = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
