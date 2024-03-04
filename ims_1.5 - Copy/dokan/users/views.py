from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

#importing forms from forms.py
from .forms import LoginForm
from .forms import SignupForm

#utility functions library from utils.py:
from .utils import generate_unique_workspace_identifier


# Create your views here.

def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    return render(request, 'users/login.html', {'form': forms})


def logout_page(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Generate unique workspace identifier
            workspace_identifier = generate_unique_workspace_identifier()
            user = form.save(commit=False)
            user.id = workspace_identifier
            user.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})