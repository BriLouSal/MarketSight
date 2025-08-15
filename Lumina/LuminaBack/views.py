from django.shortcuts import render
from django.http import HttpResponse
import yfinance as yf
import matplotlib.pyplot as plt
import csv as cs
from .models import User, Portfolio



#  This is the views.py file where we will handle the logic for our application
#  We will create views for home, portfolio room, stock, login, signup, and assistance

user = "Louie"



#  This is a list of stocks that we will use to display in the portfolio room
ticker = [
    {'id': 1, 'stock': 'AAPL'}, # We're eventually gonna add price
    {'id': 2, 'stock': 'UNH' },
    {'id': 3, 'stock': 'NVDA' },

]

def stock_information():
    # This function will fetch stock information from yfinance
    pass


def index(request):
    # This is the index view where we will display the home page/search page
    return render(request, 'base/search.html')

def home(request):
    return render(request, 'base/home.html')


def portfolio_room(request, stock_tick):
    context = {'ticker': ticker}
    return render(request, 'portfolio_room.html', context)

def stock(request):
    context = {'ticker': ticker}
    return render(request, 'base/stock.html', context)


def portfolio(request):
    return render(request, 'portfolio.html')

def signup(request):
    
    return render(request, 'signup.html')




def login(request):
    return render(request, 'login.html')


def assistance(request):
    return render(request, 'Assistance.html')









#  Create the login html, I will be using password redirects later



# def stock_portfolio(request):
#     # We will fetch user's stock portfolio from database and display it here
#     context = {}
#     return render(request, 'LuminaBack/stock_portfolio.html', context)
