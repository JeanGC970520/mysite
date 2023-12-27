from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Funciones que se ejecutaran cuando un end-point sea llamado. 
def index(request):
    return HttpResponse("Index page")

# ! Metodo que recibe un URL param llamado 'username'
def hello(request, username):
    print(f"Username: {username} of type {type(username)}")
    return HttpResponse(f"<h1>Hello {username}</h1>")

def about(request):
    return HttpResponse("About")
