from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import usuario

# Create your views here.
def home(request):
    return render(request,'Base.html')

def ajuda(request):
    return render(request,'ajuda.html')
