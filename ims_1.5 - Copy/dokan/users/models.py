# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    id = models.CharField(max_length=50, unique=True)
    # Add other custom fields as needed

    def __str__(self):
        return self.id