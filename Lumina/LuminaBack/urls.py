from django.urls import path
from django.http import HttpResponse
from . import views
import yfinance as yf



#  Append stock list when users add stock


#  We wanna get user information based on stocks


urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
    path('stock/', views.stock, name='stock'),
    path('login/', views.signup, name='login'),
    
]




# room/<str:room_number> - This will match URLs like /room/1, /room/2, and so on. The <str:room_number> part of the URL captures the room number as a string.

