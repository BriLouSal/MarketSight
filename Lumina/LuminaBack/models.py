from django.db import models

# Create your models here.

#  Creating Users 
class User(models.Model):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.username
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.name} ({self.ticker})"




#  Creating Portfolio

    









