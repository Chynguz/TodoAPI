from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)

class User(AbstractUser):
    age = models.SmallIntegerField()
    

