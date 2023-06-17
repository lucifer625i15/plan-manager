from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Register(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]
    
    def __str__(self):
        return self.email
        return self.email
    
class Task(models.Model):

    title = models.TextField()
