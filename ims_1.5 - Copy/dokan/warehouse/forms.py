from django import forms

from .models import Drop, Product, Category, Stock


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'model_number', 'manufacture_date', 'description', 'category', 'product_image', 'barcode', 'stock_count', 'barcode_number', 'brand', 'price', 'sortno', 'quantity',
                   'unit_of_measurement', 'cost_price', 'selling_price', 'weight', 'dimensions', 'expiry_date' ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'model_number': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'model_number'
            }),
            'manufacture_date': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'manufacture_date'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control', 'id': 'category'
            }),
            'product_image': forms.FileInput(attrs={
                'class': 'form-control', 'id': 'product_image'
            }),
            'barcode': forms.FileInput(attrs={
                'class': 'form-control', 'id': 'barcode'
            }),
            'stock_count': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'stock_count'
            }),
            'barcode_number': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'barcode_number'
            }),
            'brand': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'brand'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'price'
            }),
            'sortno': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'sortno'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'quantity'
            }),
            'unit_of_measurement': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'unit_of_measurement'
            }),
            'cost_price': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'cost_price'
            }),
            'selling_price': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'selling_price'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'weight'
            }),
            'dimensions': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'dimensions'
            }),
            'expiry_date': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'expiry_date'
            }),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'parent', 'code', 'category_image', 'stock_count', 'sales_margin', 'associated_products', 'notes']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'parent': forms.Select(attrs={
                'class': 'form-control', 'id': 'parent'
            }),
            'code': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'code'
            }),
            'category_image': forms.FileInput(attrs={
                'class': 'form-control', 'id': 'category_image'
            }),
            'stock_count': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'stock_count'
            }),
            'sales_margin': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'sales_margin'
            }),
            'associated_products': forms.SelectMultiple(attrs={
                'class': 'form-control', 'id': 'associated_products'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control', 'id': 'notes'
            }),
        }


class DropForm(forms.ModelForm):
    class Meta:
        model = Drop
        fields = ['name', 'address', 'city', 'postal_code', 'email', 'contact_person', 'contact_number', 'notes', 'state', 'country', 'capacity', 'available_space', 'used_space']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'address'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'city'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'postal_code'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'id': 'email'
            }),
            'contact_person': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'contact_person'
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'contact_number'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control', 'id': 'notes'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'state'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'country'
            }),
            'capacity': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'capacity'
            }),
            'available_space': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'available_space'
            }),
            'used_space': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'used_space'
            }),
        }


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'batch_number', 'quantity', 'unit_cost', 'total_cost', 'supplier', 'location', 'condition', 'status', 'category', 'delivery', 'category_image',
                   'stock_count', 'sales_margin', 'associated_products', 'notes']
        
        widgets = { 
            'product': forms.Select(attrs={
                'class': 'form-control', 'id': 'product'
            }),
            'batch_number': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'batch_number'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'quantity'
            }),
            'unit_cost': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'unit_cost'
            }),
            'total_cost': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'total_cost'
            }),
            'supplier': forms.Select(attrs={
                'class': 'form-control', 'id': 'supplier'
            }),
            'location': forms.Select(attrs={
                'class': 'form-control', 'id': 'location'
            }),
            'condition': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'condition'
            }),
            'status': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'status'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control', 'id': 'category'
            }),
            'delivery': forms.Select(attrs={
                'class': 'form-control', 'id': 'delivery'
            }),
            'category_image': forms.FileInput(attrs={
                'class': 'form-control', 'id': 'category_image'
            }),
            'stock_count': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'stock_count'
            }),
            'sales_margin': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'sales_margin'
            }),
            'associated_products': forms.SelectMultiple(attrs={
                'class': 'form-control', 'id': 'associated_products'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control', 'id': 'notes'
            }),
        }

