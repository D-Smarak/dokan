from django import forms

from .models import Season

class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['name', 'description', 'start_date', 'end_date', 'year', 'quarter', 'active', 'day', 'month', 'day_of_week', 'notes']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'start_date': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'start_date'
            }),
            'end_date': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'end_date'
            }),
            'year': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'year'
            }),
            'quarter': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'quarter'
            }),    
            'active': forms.CheckboxInput(attrs={
                'class': 'form-control', 'id': 'active'
            }),
            'day': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'day'
            }),
            'month': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'month'
            }),
            'day_of_week': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'day_of_week'
            }),
            'notes': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'notes'
            }),
        }