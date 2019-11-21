from django.db import models
from django.contrib.auth.models import User

# Cada entidad del modelo de datos se define en una clase
# Por cada clase se crea una tabla en la base de datos
class Alumno(models.Model):
	# Cada atributo de esta clase será una columna de la tabla
	dni=models.CharField(max_length=9)
	nombre=models.CharField(max_length=100)
	usuario=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	cursos=models.ManyToManyField("Curso")
	# Es necesario definir str para la presentación en pantalla dentro de
	# la administración de django
	def __str__(self):
		return self.nombre

class Curso(models.Model):
	abrev=models.CharField(max_length=4)
	denom=models.CharField(max_length=100)

	def __str__(self):
		return self.abrev
