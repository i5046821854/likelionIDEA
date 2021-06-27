from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    lat = models.FloatField(max_length=50, default='0')
    lng = models.FloatField(max_length=50, default='0')
    nickname = models.CharField(max_length=100)
    location = models.CharField(max_length=200)