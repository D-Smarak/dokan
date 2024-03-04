from django.contrib import admin
from .models import Drop, Category, Product, Stock

# Register your models here.
admin.site.register(Drop)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)