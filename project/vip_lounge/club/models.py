from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio=models.TextField(blank=True, null=True)
    phone=models.CharField(max_length=20, blank=True, null=True)
    
   
    
