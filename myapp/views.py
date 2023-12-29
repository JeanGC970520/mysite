from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

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
    return render(request, "projects/projects.html", {
        'projects' : projects,
    })

def tasks(request):
    # * Usamos el metodo get_object_or_404() para que no marque un error
    # * sino que devuelva un 404 Not Found en caso que no exista el registro.
    # task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {
        'tasks' : tasks,
    })

def createTask(request):
    # ! Para cuando el front haga un request GET, se despliegue el formulario
    if request.method == 'GET':
        
        return render(request, 'tasks/create_task.html', {
            'form' : CreateNewTask(),
        })
    # ! Para cuando desde el front se haga la peticion de crear una nueva tarea
    else:
        print(request.POST['title'])
        print(request.POST['description'])
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=2,
        )
        return redirect('tasks')

def createProject(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form' : CreateNewProject(),
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def proyectDetail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project' : project,
        'tasks' : tasks, 
    })