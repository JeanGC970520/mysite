from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Project, Task

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


def projects(request):
    # * En este caso devolvemos todos los registros de la tabla Projects.
    # * Con  un formato de lista y un tipo de respuesta JSON
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def task(request, id):
    # * Usamos el metodo get_object_or_404() para que no marque un error
    # * sino que devuelva un 404 Not Found en caso que no exista el registro.
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f"Task: {task.title}")
