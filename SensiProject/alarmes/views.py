from django.shortcuts import render, redirect, get_object_or_404
from alarmes.models import alarme


# Create your views here.
from .forms import alarmeForm


def novo_alarme(request):
    if request.method == 'POST':
        form = alarmeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'novo_alarme.html', {'form': form})
        else:
            print(form.errors)
    else:
        form = alarmeForm()
    return render(request, 'novo_alarme.html', {'form': form})


def alarmes(request):
    if request.method == 'POST':
        form = alarmeForm(request.POST)
        if form.is_valid():
            form.save()
    alarmes = alarme.objects.all()
    return render(request, 'lista_alarmes.html', {'alarmes': alarmes})


def deleta_alarme(request, id):
    alarme.objects.get(id=id).delete()
    return redirect('lista_alarmes')


def editar_alarme(request, id):
    alarme_edit = get_object_or_404( alarme, id=id)
    if request.method == 'POST':
        form = alarmeForm(request.POST, instance= alarme_edit)
        if form.is_valid():
            form.save()
            return redirect('lista_alarmes')
    else:
        form = alarmeForm(instance=alarme_edit)
    return render(request,'novo_alarme.html', {'form': form})
