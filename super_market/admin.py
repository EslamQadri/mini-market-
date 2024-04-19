from django.contrib import admin
from super_market.models import Product, OrderItem, Order, ProductHistory

# Register your models here.
admin.site.register((Product, OrderItem, Order, ProductHistory))
