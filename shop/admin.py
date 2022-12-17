from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'stock', 'price', 'image_url']

admin.site.register(Product)

