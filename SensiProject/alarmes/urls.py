from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('novo-alarme/', views.novo_alarme, name='novo_alarme'),

]