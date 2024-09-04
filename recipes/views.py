from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<b>Uma linda String HOME</b>")

def contato(request):
    return HttpResponse("<b>CONTATO</b>")

def sobre(request):
    return HttpResponse("<b>SOBRE</b>")