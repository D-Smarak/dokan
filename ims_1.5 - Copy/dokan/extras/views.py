from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import IntegrityError
from django.forms import ModelForm
from users.models import CustomUser
from .models import Season
from .forms import SeasonForm

# Create your views here.

# Season views
@login_required(login_url='login')
def create_season(request):
    forms = SeasonForm()
    workspace_identifier = request.user.id
    if request.method == 'POST':
        forms = SeasonForm(request.POST)
        if forms.is_valid():
            season_instance = forms.save(commit=False)  # Save form data without committing to database
            season_instance.workspace_identifier = workspace_identifier  # Assign workspace identifier
            season_instance.save()  # Save the instance with workspace identifier
            return redirect('season-list')
    context = {
        'form': forms
    }
    return render(request, 'extras/create_season.html', context)


@login_required(login_url='login')
def season_list(request):
    # Retrieve the workspace identifier of the current user
    workspace_identifier = request.user.id
    # Filter Season objects based on the workspace identifier
    seasons = Season.objects.filter(workspace_identifier=workspace_identifier)
    return render(request, 'extras/season_list.html', {'seasons': seasons})