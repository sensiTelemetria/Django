from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('novo-relatorio/', views.novo_relatorio, name='novo_relatorio'),
    path('lista-relatorios/', views.relatorios, name='lista_relatorios'),
    path('deleta-relatorio/<id>', views.deleta_relatorio, name='deleta_relatorio'),
    path('editar-relatorio/<id>', views.editar_relatorio, name='editar_relatorio'),
]