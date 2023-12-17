from django.urls import path

from . import views

# Router de los end-points
urlpatterns = [
    path("", views.hello),
    path("about/", views.about),
]