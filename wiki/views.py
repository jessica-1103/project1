from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulo

# Create your views here.
def index(request):
    return render(request,'test.html')

def articulo(request,articulo_id):
    articulo = Articulo.objects.get(pk=articulo_id)
    return render(request,'articulo.html', {'articulo':articulo._dict_})

