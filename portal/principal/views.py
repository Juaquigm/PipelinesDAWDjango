from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Vista asociada al registro de nuevos usuarios
def registro_view(request):
	# Si el usuario ya ha iniciado sesión se le redirige al raíz
	if request.user.username:
		return redirect("/")

	# En las vistas que reciban datos de un formulario se diferencia el comportamiento
	# cuando entra por primera vez sin recibir datos y cuando ya ha completado
	# el formulario y se reciben datos
	if request.POST:
		# Se ha completado el formulario
		# Se incorporan los datos recibidos al formulario
		formulario = FormRegistro(request.POST)
		# En nuevo_nombre cargamos el nombre de usuario seleccionado
		nuevo_nombre = request.POST['nombre_usuario']
		# Se comprueba que el nombre no exista
		usuario = User.objects.filter(username=nuevo_nombre)
		if len(usuario)>0:
			# Si el nombre existe se vuelve a solicitar la información
			return render(request, "registro.html", {'form':formulario, 'mensaje':"Nombre de usuario existente"})
		# Se da de alta al usuario en Django. OJO: email y password fijos para evitar complicaciones
		usuario = User.objects.create_user(nuevo_nombre,"pregunta@me.es", "gonzalo")
		# Se consolida el alta
		usuario.save()
		# Se crea un nuevo objeto del modelo con los datos del formulario
		nuevo_alumno = formulario.save()
		# Se incorpora al modelo el enlace con el nuevo usuario creado en Djando
		nuevo_alumno.usuario = usuario
		# Se consolida el objeto creado (se almacena en la BD)
		nuevo_alumno.save()
		# Se redirige al login
		return redirect("/login/")
	else:
		# Entrada inicial sin datos
		# Se inicializa el formulario
		formulario = FormRegistro()
	# Se renderiza la plantilla con el formulario
	return render(request, "registro.html", {'form':formulario})

# Formulario de login
def login_view(request):
	# Si el usuario ya ha iniciado sesión se le redirige al raíz
	if request.user.username:
		return redirect("/")
	
	# En las vistas que reciban datos de un formulario se diferencia el comportamiento
	# cuando entra por primera vez sin recibir datos y cuando ya ha completado
	# el formulario y se reciben datos
	if request.POST:
		# Se han recibido datos
		# Se incorporan los datos recibidos al formulario
		formulario = FormLogin(request.POST)
		# Se comprueba si la combinación ususario/clave es correcta
		user = authenticate(username=request.POST['nombre'], password=request.POST['password'])
		if user is not None:
			# Si es correcta se procede a iniciar sesión
			login(request, user)
			# Se redirige al raíz
			return redirect("/")
	else:
		# Se inicializa el formulario
		formulario = FormLogin()
	# Se renderiza la plantilla con el formulario
	return render(request, "login.html", {'form':formulario})

# Vista de logout
def logout_view(request):
	# El logout funciona aunque no se haya iniciado sesión
	logout(request)
	return redirect("/")

# Vista principal
# Decorador que exige sesión iniciada, si no redirige a login
@login_required(login_url="/login")
def index(request):
	# Recupera la información como alumno asociada al usuario Django
	try:
		alumno = Alumno.objects.get(usuario = request.user)
	except ObjectDoesNotExist:
		# Si el usuario no tiene asociado datos de alumno se redirige al logout
		# para evitar problemas
		return redirect("/logout/")

	# Se selecionan los cursos asociados al alumno
	cursos = alumno.cursos.all()
	# Se renderiza una vista simple con la lista de cursos seleccionada
	return render(request, "index.html", {'usuario':request.user, 'cursos':cursos})