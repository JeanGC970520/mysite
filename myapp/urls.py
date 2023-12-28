from django.urls import path

from . import views

# Router de los end-points
urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    # ! IMPORTANTE: Definicion de un URL param. 
    # ! El cual es de tipo str y se llamara 'username', el metodo hello() del modulo views
    # ! tendra que recibir dicho parametro y hacer la operacion correspondiente.
    path("hello/<str:username>", views.hello),
    path("projects/", views.projects),
    path("task/", views.task),
    path("create_task/", views.createTask),
]