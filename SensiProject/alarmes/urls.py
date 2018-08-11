from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('novo-alarme/', views.novo_alarme, name='novo_alarme'),
    path('lista-alarmes/',views.alarmes, name='lista_alarmes'),
    path('deleta-alarme/<id>', views.deleta_alarme, name='deleta_alarme'),
    path('editar-alarme/<id>', views.editar_alarme, name='editar_alarme'),

]