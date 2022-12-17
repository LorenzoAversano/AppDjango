from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField()