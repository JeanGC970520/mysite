from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Project, Task

# Create your views here.
# Funciones que se ejecutaran cuando un end-point sea llamado. 
def index(request):
    title = 'Django Course!!'
    # ! Enviando datos al archivo HTML, que en realidad es un template que el Motor
    # ! de Plantillas procesara y convertira finalmente en un HTML para el navegador.
    return render(request, "index.html", {
        'title' : title,
    })

# ! Metodo que recibe un URL param llamado 'username'
def hello(request, username):
    print(f"Username: {username} of type {type(username)}")
    return HttpResponse(f"<h1>Hello {username}</h1>")

def about(request):
    username = 'Jeanveloper'
    return render(request, "about.html", {
        'username' : username,
    })


def projects(request):
    # * En este caso devolvemos todos los registros de la tabla Projects.
    # * Con  un formato de lista y un tipo de respuesta JSON
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects.html", {
        'projects' : projects,
    })

def task(request):
    # * Usamos el metodo get_object_or_404() para que no marque un error
    # * sino que devuelva un 404 Not Found en caso que no exista el registro.
    # task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, "task.html", {
        'tasks' : tasks,
    })
