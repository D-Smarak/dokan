from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'buyer', 'customer', 'description', 'quantity', 'sales_date', 'payment_method', 'total_amount', 'tax_amount', 'discount_amount', 'sub_total', 'payment_status', 
                    'tranasaction_id', 'tracking_number', 'notes', 'quantity', 'supplier', 'location', 'status', 'category', 'delivery']

        widgets = { 
            'product': forms.Select(attrs={
                'class': 'form-control', 'id': 'product'
            }),
            'buyer': forms.Select(attrs={
                'class': 'form-control', 'id': 'buyer'
            }),
            'customer': forms.Select(attrs={
                'class': 'form-control', 'id': 'customer'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'quantity'
            }),
            'sales_date': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'sales_date'
            }),
            'payment_method': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'payment_method'
            }),
            'total_amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'total_amount'
            }),
            'tax_amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'tax_amount'
            }),
            'discount_amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'discount_amount'
            }),
            'sub_total': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'sub_total'
            }),
            'payment_status': forms.Select(attrs={
                'class': 'form-control', 'id': 'payment_status'
            }),
            'tranasaction_id': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'tranasaction_id'
            }),
            'tracking_number': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'tracking_number'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control', 'id': 'notes'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'quantity'
            }),
            'supplier': forms.Select(attrs={
                'class': 'form-control', 'id': 'supplier'
            }),
            'location': forms.Select(attrs={
                'class': 'form-control', 'id': 'location'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control', 'id': 'category'
            }),
            'delivery': forms.Select(attrs={
                'class': 'form-control', 'id': 'delivery'
            }),
            
        }