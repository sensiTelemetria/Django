from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def home(Request):
    return HttpResponse("<h1>Hello WorlAd222222</h1>")