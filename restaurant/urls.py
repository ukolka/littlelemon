from django.contrib import admin
from django.urls import path
from restaurant import views

urlpatterns = [
    path('', views.index, name='index'),
]

