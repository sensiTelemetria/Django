from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('novo-usuario/', views.novo_usuario, name='novo_usuario'),
]