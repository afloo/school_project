# store/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('form',views.form,name='form'),
    path('order', views.order, name='order'),
    path('department',views.allDpt, name='allDpt'),
    # Add other paths as needed
]

