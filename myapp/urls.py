from django.urls import path

from . import views

# Router de los end-points
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    # ! IMPORTANTE: Definicion de un URL param. 
    # ! El cual es de tipo str y se llamara 'username', el metodo hello() del modulo views
    # ! tendra que recibir dicho parametro y hacer la operacion correspondiente.
    path("hello/<str:username>", views.hello, name="hello"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:id>", views.proyectDetail, name="project_detail"),
    path("tasks/", views.tasks, name="tasks"),
    path("create_task/", views.createTask, name="create_task"),
    path("create_project/", views.createProject, name="create_project"),
]