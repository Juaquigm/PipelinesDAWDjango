from django.contrib import admin
from . import models

# Registramos las entidades del modelo en la administración de Django
admin.site.register(models.Alumno)
admin.site.register(models.Curso)