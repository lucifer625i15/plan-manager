from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Task(models.Model):

    title = models.TextField()
    desc = models.TextField()
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    priority =models.CharField(max_length=10)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.title