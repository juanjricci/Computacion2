from tkinter import CASCADE
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Carreras(models.Model):
    nombre_carrera = models.CharField(max_length=100)
    horarios_cursado = models.CharField(max_length=1024)
    plan_correlatividades = models.CharField(max_length=1024)
    calendario_academico = models.CharField(max_length=1024)
    mesas = models.CharField(max_length=1024)

    def __str__(self):
        return self.nombre_carrera

class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    codigo_carrera = models.ForeignKey(Carreras, on_delete=CASCADE)

    def __str__(self):
        return self.nombre
