from django.contrib.auth.models import User
from django.db import models

from ecomm.managers import ApproximateCountManager, InfiniteCountManager


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True, max_length=512)
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Price in USD ($)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (${self.price})"


class Purchase(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address = models.TextField(max_length=512)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = InfiniteCountManager()

    def __str__(self):
        return f"Purchase #{self.id}"
