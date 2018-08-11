from django.shortcuts import render, redirect, get_object_or_404
from relatorios.models import relatorio

# Create your views here.

from .forms import relatorioForm


def novo_relatorio(request):
    if request.method == 'POST':
        form = relatorioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'novo_relatorio.html', {'form': form})
        else:
            print(form.errors)
    else:
        form = relatorioForm()
    return render(request, 'novo_relatorio.html', {'form': form})


def relatorios(request):
    if request.method == 'POST':
        form = relatorioForm(request.POST)
        if form.is_valid():
            form.save()
    relatorios = relatorio.objects.all()
    return render(request, 'lista_relatorios.html', {'relatorios': relatorios})

def deleta_relatorio(request, id):
    relatorio.objects.get(id=id).delete()
    return redirect('lista_relatorios.html')

def editar_relatorio(request, id):
    relatorio_edit = get_object_or_404( relatorio, id=id)
    if request.method == 'POST':
        form = relatorioForm(request.POST, instance= relatorio_edit)
        if form.is_valid():
            form.save()
            return redirect('lista_relatorios.html')
    else:
        form = relatorioForm(instance=relatorio_edit)
    return render(request,'novo_relatorio.html', {'form': form})
