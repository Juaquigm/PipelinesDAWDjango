import django.forms as forms
from .models import *

# Formulario basado en un modelo
class FormRegistro(forms.ModelForm):
	# Este elemento se añade a los atributos del modelo
	nombre_usuario = forms.CharField(max_length = 20)
	# Con esta clase definimos el modelo de referencia del formulario
	class Meta:
		model = Alumno
		# Indicamos qué atributos se incluyen en el formulario
		fields = ['dni', 'nombre', 'cursos' ]

# Formulario independiente del modelo
class FormLogin(forms.Form):
	# Se incluyen los siguientes elementos en el formulario
	nombre = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20, widget=forms.PasswordInput)