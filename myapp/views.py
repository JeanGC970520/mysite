from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Funciones que se ejecutaran cuando un end-point sea llamado. 
def hello(request):
    return HttpResponse("<h1>Hello world</h1>")

def about(request):
    return HttpResponse("About")
