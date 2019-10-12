from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
    
class Customer(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profile/', default='useravatar.png')
