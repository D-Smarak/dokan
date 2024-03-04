from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

'''
This approach is used when you want to create a form that is not directly linked to a Django model.
You define the form fields and their properties manually
'''
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))


'''
This approach is used when you want to create a form that is directly linked to a Django model. 
By specifying the model attribute in the Meta class, Django automatically generates form fields 
based on the model's fields.You can still customize the form fields using the widgets attribute 
in the Meta class to add HTML attributes or change the widget used for rendering the field
'''

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')