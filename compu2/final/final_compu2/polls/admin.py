from django.contrib import admin
from .models import Carreras, Alumnos

# Register your models here.
class CarrerasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_carrera', 'horarios_cursado', 'plan_correlatividades', 'calendario_academico', 'mesas')

class AlumnosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'codigo_carrera')


admin.site.register(Carreras, CarrerasAdmin)
admin.site.register(Alumnos, AlumnosAdmin)