from django.contrib import admin

# Register your models here.
from .models import (
    Supplier,
    Buyer,
    Customer,
    Delivery,
)



class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'supplier_name', 'address','email','contact_number','created_date']
    ordering =  ['id']
    search_fields = ['company_name', 'supplier_name']


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer_name', 'address', 'email', 'contact_number', 'created_date']
    ordering =  ['id']
    search_fields = ['buyer_name']

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Customer)
admin.site.register(Delivery)