from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from alarmes.models import alarme


# Create your views here.
from .forms import alarmeForm


def novo_alarme(request):
    if request.method == 'POST':
        form = alarmeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Alarme adicionado com sucesso')
        else:
            print(form.errors)
    else:
        form = alarmeForm()

    return render(request, 'novo_alarme.html', {'form': form})



def alarmes(request):
    alarmes = alarme.objects.all()
    return render(request,'lista_alarmes.html', {'alarmes': alarmes})

def deleta_alarme(request, id):
    alarme.objects.get(id=id).delete()
    return redirect('lista_alarmes.html')

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



