from django.contrib import admin
from django.urls import path
from App_Django.Tarefa import views

urlpatterns = [
    path(r'nova-categoria',views.nova_categoria , name = 'nova_categoria'),
    path(r'lista-categoria',views.lista_categoria , name = 'lista_categoria'),
    path('admin/', admin.site.urls),
    path(r"nova-tarefa",views.nova_tarefa, name = "nova_tarefa"),
    path(r"delete-tarefa/<int:id>",views.delete_tarefa, name = "delete_tarefa"),
    path(r"delete-tarefa-search/<int:id>/<str:q>",views.delete_tarefa_search, name = "delete_tarefa_search"),
    path(r"editar-tarefa/<int:id>",views.editar_tarefa, name = "editar_tarefa"),
    path(r"editar-categoria/<int:id>",views.editar_categoria, name = "editar_categoria"),
    path(r"delete-categoria/<int:id>",views.delete_categoria, name = "delete_categoria"),
    path(r"buscar/",views.search, name = "search"),
]
