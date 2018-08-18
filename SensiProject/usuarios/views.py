from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from usuarios.models import usuario
from django.contrib.auth.decorators import login_required


# Create your views here.
from .forms import usuarioForm


def novo_usuario(request):
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'novo_usuario.html', {'form': form})
        else:
            print(form.errors)
    else:
        form = usuarioForm()
    return render(request, 'novo_usuario.html', {'form': form})


def usuarios(request):
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()
    usuarios = usuario.objects.all()
    return render(request, 'lista_usuarios', {'usuarios': usuarios})

def deleta_usuario(request, id):
    usuario.objects.get(id=id).delete()
    return redirect('lista_usuarios')

def editar_usuario(request, id):
    usuario_edit = get_object_or_404( usuario, id=id)
    if request.method == 'POST':
        form = usuarioForm(request.POST, instance= usuario_edit)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = usuarioForm(instance=usuario_edit)
    return render(request,'novo_usuario.html', {'form': form})


