from django import forms

from .models import Supplier, Buyer, Customer, Delivery


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['company_name', 'supplier_name', 'address', 'email', 'contact_number', 'amount_allocated', 'contract_expiry', 'notes', 'credit_limit', 
                    'city', 'postal_code', 'lead_time', 'website', 'category']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'company_name',
                'data-val': 'true',
                'data-val-required': 'Please enter company name',
            }),
            'supplier_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'supplier_name',
                'data-val': 'true',
                'data-val-required': 'Please enter supplier name',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'address',
                'data-val': 'true',
                'data-val-required': 'Please enter address',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'data-val': 'true',
                'data-val-required': 'Please enter email',
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'contact_number',
                'data-val': 'true',
                'data-val-required': 'Please enter contact number',
            }),
            'amount_allocated': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'amount_allocated',
                'data-val': 'true',
                'data-val-required': 'Please enter amount allocated',
            }),
            'contract_expiry': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'contract_expiry',
                'data-val': 'true',
                'data-val-required': 'Please enter contract expiry',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'notes',
                'data-val': 'true',
                'data-val-required': 'Please enter notes',
            }),
            'credit_limit': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'credit_limit',
                'data-val': 'true',
                'data-val-required': 'Please enter credit limit',
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'city',
                'data-val': 'true',
                'data-val-required': 'Please enter city',
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'postal_code',
                'data-val': 'true',
                'data-val-required': 'Please enter postal code',
            }),
            'lead_time': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'lead_time',
                'data-val': 'true',
                'data-val-required': 'Please enter lead time',
            }),
            'website': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'website',
                'data-val': 'true',
                'data-val-required': 'Please enter website',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'id': 'category',
                'data-val': 'true',
                'data-val-required': 'Please select category',
            }),
        }


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['buyer_name', 'company_name', 'address', 'email', 'contact_number', 'amount_allocated', 'contract_expiry', 'notes', 'credit_limit']
        widgets = {
            'buyer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'buyer_name',
                'data-val': 'true',
                'data-val-required': 'Please enter buyer name',
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'company_name',
                'data-val': 'true',
                'data-val-required': 'Please enter company name',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'address',
                'data-val': 'true',
                'data-val-required': 'Please enter address',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'data-val': 'true',
                'data-val-required': 'Please enter email',
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'contact_number',
                'data-val': 'true',
                'data-val-required': 'Please enter contact number',
            }),
            'amount_allocated': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'amount_allocated',
                'data-val': 'true',
                'data-val-required': 'Please enter amount allocated',
            }),
            'contract_expiry': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'contract_expiry',
                'data-val': 'true',
                'data-val-required': 'Please enter contract expiry',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'notes',
                'data-val': 'true',
                'data-val-required': 'Please enter notes',
            }),
            'credit_limit': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'credit_limit',
                'data-val': 'true',
                'data-val-required': 'Please enter credit limit',
            }),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'company_name', 'address', 'email', 'contact_number', 'amount_allocated', 'contract_expiry', 'notes', 'credit_limit']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'customer_name',
                'data-val': 'true',
                'data-val-required': 'Please enter customer name',
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'company_name',
                'data-val': 'true',
                'data-val-required': 'Please enter company name',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'address',
                'data-val': 'true',
                'data-val-required': 'Please enter address',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'data-val': 'true',
                'data-val-required': 'Please enter email',
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'contact_number',
                'data-val': 'true',
                'data-val-required': 'Please enter contact number',
            }),
            'amount_allocated': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'amount_allocated',
                'data-val': 'true',
                'data-val-required': 'Please enter amount allocated',
            }),
            'contract_expiry': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'contract_expiry',
                'data-val': 'true',
                'data-val-required': 'Please enter contract expiry',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'notes',
                'data-val': 'true',
                'data-val-required': 'Please enter notes',
            }),
            'credit_limit': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'credit_limit',
                'data-val': 'true',
                'data-val-required': 'Please enter credit limit',
            }),
        }

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['delivery_name', 'email', 'contact_number', 'partner_type', 'area_coverage', 'shipping_rates', 'manager_name', 'contract_expiry', 'notes']
        widgets = {
            'delivery_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'delivery_name',
                'data-val': 'true',
                'data-val-required': 'Please enter delivery name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'data-val': 'true',
                'data-val-required': 'Please enter email',
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'contact_number',
                'data-val': 'true',
                'data-val-required': 'Please enter contact number',
            }),
            'partner_type': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'partner_type',
                'data-val': 'true',
                'data-val-required': 'Please enter partner type',
            }),
            'area_coverage': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'area_coverage',
                'data-val': 'true',
                'data-val-required': 'Please enter area coverage',
            }),
            'shipping_rates': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'shipping_rates',
                'data-val': 'true',
                'data-val-required': 'Please enter shipping rates',
            }),
            'manager_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'manager_name',
                'data-val': 'true',
                'data-val-required': 'Please enter manager name',
            }),
            'contract_expiry': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'contract_expiry',
                'data-val': 'true',
                'data-val-required': 'Please enter contract expiry',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'notes',
                'data-val': 'true',
                'data-val-required': 'Please enter notes',
            }),
        }