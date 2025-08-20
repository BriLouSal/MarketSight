from django.db import models

# Create your models here.

#  Creating Users 
class Profile(models.Model):
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



class Message (models.Model):
    user_message = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user_message[0:200] 
#  Creating Portfolio





class Transaction (models.Model):
    bought_date = models.DateTimeField(auto_now_add = True)
    user_owned = models.ForeignKey()

    









