from django.db import models

# Create your models here.

#  Creating Users 
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

#  Stock's Name and Symbol
class Stock(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, unique=True)

#  Stock's Price and Date
class StockPrice(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()




    







