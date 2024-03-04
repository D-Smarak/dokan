from django.db import models
from django.core.files.base import ContentFile
from warehouse.models import Category

# Create your models here.
class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=120, null=False)
    supplier_name = models.CharField(max_length=120, unique=True, null=False)
    address = models.CharField(max_length=220, null=False)
    city = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=254, unique=True, null=True)
    contact_number = models.CharField(max_length=20, unique=True, null=False)
    lead_time = models.IntegerField(null=True)
    notes = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    contract_expiry = models.DateField(null=True, blank=True)
    amount_allocated = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_date = models.DateField(auto_now_add=True)
    workspace_identifier = models.CharField(max_length=50)  # Add the workspace_identifier field

    def __str__(self):
        return self.supplier_name


class Buyer(models.Model):
    id = models.AutoField(primary_key=True)  # Add new primary key field
    buyer_name = models.CharField(max_length=120, null=False)
    company_name = models.CharField(max_length=120, null=True)
    address = models.CharField(max_length=220, null=False)
    email = models.EmailField(max_length=254, default='Null', unique=True, null=True)
    contact_number = models.CharField(max_length=20, unique=True, null=False)
    amount_allocated = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    notes = models.TextField(blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    contract_expiry = models.DateField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    workspace_identifier = models.CharField(max_length=50)

    def __str__(self):
        return self.buyer_name


class Customer(models.Model):
    id = models.AutoField(primary_key=True)  # Add new primary key field
    customer_name = models.CharField(max_length=120, null=False)
    company_name = models.CharField(max_length=120, null=True)
    address = models.CharField(max_length=220, null=False)
    email = models.EmailField(max_length=254, default='Null', unique=True, null=True)
    contact_number = models.CharField(max_length=20, unique=True, null=False)
    amount_allocated = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    notes = models.TextField(blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    contract_expiry = models.DateField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    workspace_identifier = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name
    

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    delivery_name = models.CharField(max_length=120, null=False)
    email = models.EmailField(max_length=254, default='Null', unique=True, null=True)
    contact_number = models.CharField(max_length=20, unique=True, null=False)
    partner_type = models.CharField(max_length=100, null=True)
    area_coverage = models.CharField(max_length=100, null=True)
    shipping_rates = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    manager_name = models.CharField(max_length=100, null=False)
    contract_expiry = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    workspace_identifier = models.CharField(max_length=50)

    def __str__(self):
        return self.delivery_name
