from django.db import models

# Create your models here.

#  Creating Users 
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    pfp = models.ImageField()
    email = models.EmailField(unique=True)


    







