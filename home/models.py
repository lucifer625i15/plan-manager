from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Register(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.TextField()
    last_name = models.TextField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.email