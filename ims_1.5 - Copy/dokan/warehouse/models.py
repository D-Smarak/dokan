from django.db import models
from django.core.files import File
from partners.models import Supplier, Delivery

from barcode import get_barcode
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from barcode.writer import ImageWriter


# Create your models here.
class Drop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, unique=True, null=False)
    address = models.CharField(max_length=220, null=False)
    city = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=254, unique=True, null=True)
    contact_person = models.CharField(max_length=20, unique=True, null=False)
    contact_number = models.CharField(max_length=20, unique=True, null=False)
    notes = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    capacity = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    available_space = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    used_space = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_date = models.DateField(auto_now_add=True)
    workspace_identifier = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, null=False)
    description = models.TextField(default='Null', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    code = models.PositiveIntegerField(default=0, unique=True, null=False)
    created_date = models.DateField(auto_now_add=True)
    category_image = models.ImageField(null=True, blank=True, upload_to='images/category/')
    workspace_identifier = models.CharField(max_length=50) 
    stock_count = models.PositiveIntegerField(default=0, null=True)
    sales_margin = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, null=True)
    associated_products = models.ManyToManyField('Product', related_name='categories', blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, null=False)
    description = models.TextField(default='Null', null=True, blank=True)
    manufacture_date = models.DateField(null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    model_number = models.CharField(max_length=50, default='Null', unique=True)
    barcode_number = models.CharField(max_length=50, default='Null', unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,  null=False)
    sortno = models.PositiveIntegerField(default=0, unique=True, null=False)
    quantity = models.PositiveIntegerField(null=True)
    unit_of_measurement = models.CharField(max_length=50, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=100,  null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    barcode = models.ImageField(upload_to='images/', blank=True)
    product_image = models.ImageField(null=True, blank=True, upload_to='images/product/')
    workspace_identifier = models.CharField(max_length=50)
    stock_count = models.PositiveIntegerField(default=0, unique=True)

    def __str__(self):
        return self.name
    
    def save(self, id, name, model_num, manufacture_date, *args, **kwargs):
        barcode_input = f'{id}-{name}-{model_num}-{manufacture_date}'
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(barcode_input, writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)


class Stock(models.Model):

    STATUS_CHOICE = (
        ('ok', 'Ok'),
        ('recheck', 'Recheck'),
        ('damaged', 'Damaged'),
        ('lost', 'Lost'),
        ('rejected', 'Rejected'),
    )

    CONDITION_CHOICE = (
        ('new', 'New'),
        ('used', 'Used'),
        ('refurbished', 'Refurbished'),
    )

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    batch_number = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Drop, on_delete=models.SET_NULL, null=True, blank=True)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL)
    category_image = models.ImageField(null=True, blank=True, upload_to='images/category/')
    workspace_identifier = models.CharField(max_length=50)
    stock_count = models.PositiveIntegerField(default=0, null=True)
    sales_margin = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, null=True)
    associated_products = models.ManyToManyField('Product', related_name='categories', blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.id
    

