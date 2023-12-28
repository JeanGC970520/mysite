from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # ! Relacionar tablas.
    # ! Para relacionar las tablas usamos un ForeingKey y en este caso cuando se elimine un 
    # ! un Project, todo lo relacionado con el queremos que tambien se elimine, por lo cual
    # ! usamos el param on_delete en modo CASCADE.
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.project.name}" 