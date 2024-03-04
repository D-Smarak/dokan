from django.db import models
from django.core.files.base import ContentFile

# Create your models here.
class Season(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, null=False)
    description = models.TextField(default='Null', null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    year = models.PositiveIntegerField(null=True)
    quarter = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=False)
    day = models.PositiveIntegerField(null=True)
    month = models.PositiveIntegerField(null=True)
    day_of_week = models.CharField(max_length=255, unique=True, null=False)
    notes = models.TextField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    workspace_identifier = models.CharField(max_length=50) 

    def __str__(self):
        return self.name
    
