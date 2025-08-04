from django.shortcuts import render
from django.http import HttpResponse
import yfinance as yf
import matplotlib.pyplot as plt
import csv as cs



user = "Louie"




ticker = [
    {'id': 1, 'stock': 'AAPL'}, # We're eventually gonna add price
    {'id': 2, 'stock': 'UNH' },
    {'id': 3, 'stock': 'NVDA'},

]




def home(request):
    return render(request, 'home.html')


def room(request):
    context = {'ticker': ticker}
    return render(request, 'portfolio_room.html', context)

def stock(request):
    return render(request, 'stock.html')


def portfolio(request):
    return render(request, 'portfolio.html')

def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')











#  Create the login html, I will be using password redirects later



# def stock_portfolio(request):
#     # We will fetch user's stock portfolio from database and display it here
#     context = {}
#     return render(request, 'LuminaBack/stock_portfolio.html', context)
