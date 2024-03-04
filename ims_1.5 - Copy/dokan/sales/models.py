from django.db import models
from django.core.files.base import ContentFile
from partners.models import Supplier, Delivery, Buyer, Customer
from warehouse.models import Drop, Category, Product

# Create your models here.

class Order(models.Model):

    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    PAYMENT_CHOICE = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('overdue', 'Overdue'),
    )

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(default='Null', null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True)
    sales_date = models.DateField(null=True, blank=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, null=False) 
    tax_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2, null=True)
    discount_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2, null=True)
    sub_total = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICE)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    tracking_number = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Drop, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL)
    workspace_identifier = models.CharField(max_length=50)

    def __str__(self):
        return self.id
    


