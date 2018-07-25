from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from .forms import usuarioForm


def novo_usuario(request):
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, '../../usuarios/templates/novo_usuario.html', {'form': form})
        else:
            print(form.errors)
    else:
        form = usuarioForm()

    return render(request, '../../usuarios/templates/novo_usuario.html', {'form': form})
