from django.urls import path
from . import views
from .views import (
    create_season, 
    season_list,
)

urlspatterns = [
    path('create-season/', create_season, name='create-season'),
    path('season-list/', season_list, name='season-list'),
]