from django.shortcuts import render,redirect
from django.http import HttpResponse
from App_Django.Tarefa.models import Categoria, Tarefa
from .forms import CategoriaForm,TarefaForm
from .models import Tarefa,Categoria
from django.contrib.auth.decorators import login_required
from    django.contrib import messages

# Create your views here.
@login_required
def Home(request):

    tarefas = Tarefa.objects.filter(user =  request.user)

    return render(request,"tarefa/index.html",{"tarefas":tarefas})

@login_required
def lista_categoria(request):

    categoria = Categoria.objects.filter(user =  request.user)

    return render(request,"tarefa/lista_categoria.html",{"categoria":categoria})

@login_required
def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect("/tarefa/lista-categoria")


        else:
            print(form.errors)
    else:
        form = CategoriaForm()
    #return render(request,'tarefas/nova_categoria.html', {'form':form})
    return render(request, 'tarefa/nova_categoria.html', {'form':form})

@login_required
def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(user=request.user, data= request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect("/")

        else:
            print(form.errors)
    else:
        form = TarefaForm(user = request.user)
    return render(request,'tarefa/nova_tarefa.html', {'form':form})

@login_required
def delete_tarefa_search(request,id,q):
    tarefa_del = Tarefa.objects.get(id = id,user = request.user)

    print(tarefa_del.user)
    print(request.user)

    if tarefa_del.user == request.user:
        tarefa_del.delete()

        result = Tarefa.objects.search(q, request)

        return render(request, "tarefa/paginas_resultados.html", {"result": result,'q':q})
        #return render(request, 'tarefa/index.html')

    else:
        messages.error(request, "Sem permissão")

    return redirect("/")

def delete_tarefa(request,id):

    tarefa = Tarefa.objects.get(id = id,user = request.user)

    if tarefa.user == request.user:
        tarefa.delete()
        return render(request, 'tarefa/index.html')
    else:
        messages.error(request, "Sem permissão")

    return redirect("/")


@login_required
def editar_tarefa(request,id):

    tarefa = Tarefa.objects.get(id = id,user = request.user)

    if request.method == 'POST':

        form = TarefaForm(user = request.user, data = request.POST,instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            print(form.errors)
    else:
        form =  TarefaForm(user=request.user, instance=tarefa)
    return render(request, 'tarefa/nova_tarefa.html', {'form': form})

@login_required
def editar_categoria(request,id):
    categoria = Categoria.objects.get(id = id,user = request.user)

    if request.method == "POST":
        form = CategoriaForm(request.POST, instance= categoria)
        if form.is_valid():
            form.save()
            return redirect("/tarefa/lista-categoria")
        else:
            print(form.errors)
    else:
        form = CategoriaForm(instance= categoria)
    return render(request, "tarefa/nova_categoria.html",{"form":form})



@login_required
def delete_categoria(request,id):
    categoria =  Categoria.objects.get(id = id,user = request.user)
    print( categoria.user ,  request.user )
    if categoria.user == request.user:
        categoria.delete()
        return render(request, 'tarefa/lista_categoria.html')
    else:
        messages.error(request, "Sem permissão")

    return redirect("/tarefa/lista-categoria")

@login_required
def search(request):

    q = request.GET.get("search")
    print(q)

    if q is not "":

        result = Tarefa.objects.search(q,request)

        return render(request,"tarefa/paginas_resultados.html",{'result':result,'q':q})

    return redirect("/")