from django.db import models

class Product(models.Model):
    INVENTORY_STATUS_CHOICES = [
        ("INSTOCK", "In Stock"),
        ("LOWSTOCK", "Low Stock"),
        ("OUTOFSTOCK", "Out of Stock"),
    ]

    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    internalReference = models.CharField(max_length=100, blank=True, null=True)
    shellId = models.IntegerField()
    inventoryStatus = models.CharField(max_length=20, choices=INVENTORY_STATUS_CHOICES)
    rating = models.FloatField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
