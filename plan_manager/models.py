from django.contrib.auth.models import Group, Permission
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    groups = models.ManyToManyField(Group, related_name='task_manager_users')
    user_permissions = models.ManyToManyField(
        Permission, related_name='task_manager_users'
    )
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username