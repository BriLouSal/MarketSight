from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import csv as cs
from .models import Profile, Portfolio



#  This is the views.py file where we will handle the logic for our application
#  We will create views for home, portfolio room, stock, login, signup, and assistance

user = "Louie"



#  This is a list of stocks that we will use to display in the portfolio room
ticker = []



def check_stock(ticker_symbol):
    stock_info = None # We'll use this for try/exception to display yfinance data
    pass



def search(request):
    # This is the index view where we will display the home page/search page
    # Now we need to find how to redirect the search html -> stock.html



    return render(request, 'base/search.html')

def home(request):
    return render(request, 'base/home.html')


def portfolio_room(request):
    context = {'ticker': ticker}
    return render(request, 'portfolio_room.html', context)

def stock(request, stock_tick):
    stock_info = None
    for i in ticker:
        if i['id'] == str(stock_tick):
            stock_info = i
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
