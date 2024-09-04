from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Leonardo Franklin',
    })

def contato(request):
    return HttpResponse("<b>CONTATO</b>")

def sobre(request):
    return HttpResponse("<b>SOBRE</b>")