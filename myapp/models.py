from django.db import models
from django.contrib.auth.models import User

# Create your models here.from django.contrib.auth.models import User

class Myuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Address = models.CharField(max_length=120)
    City = models.CharField(max_length=100)
    Age = models.IntegerField()
    PhoneNumber= models.IntegerField()
    
class Shedular(models.Model):
    url=models.URLField()
    time=models.DateTimeField()
    