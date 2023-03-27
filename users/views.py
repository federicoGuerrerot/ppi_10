from django.contrib.auth import authenticate, get_user_model, login, logout # Para autenticar, crear usuarios y cerrar sesión
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password # Para encriptar la contraseña
from django.http.response import HttpResponse, JsonResponse

from users.forms import FormCrearUsuario

def user_login(request):
    """Función para iniciar sesión, se encarga de autenticar al usuario y de redirigir a la pagina principal
    si este existe y las credenciales son correctas, de lo contrario muestra un mensaje de error"""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../..')  
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrecta')
    return render(request, 'users/login.html')

def user_signup(request):
    """Función para crear un nuevo usuario y de redirigir a la pagina principal una vez registrado
    En caso de que el usuario ya exista o alguna credencial sea invalida, se muestra un mensaje de error"""
    
    if request.method == 'POST':
        form = FormCrearUsuario(request.POST)
        if form.is_valid():
            email = request.POST['email']
            nombre = request.POST['nombre']
            password = request.POST['password1']
            user = form.save(commit=False)
            user.save()
            form.save_m2m() # Para guardar los campos ManyToMany (tags:Temas)
            #user = authenticate(request, email=email, nombre=nombre, password=password)
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')

            return redirect('../..')
            #return JsonResponse({'username/email': f'{email}','nombre': f'{nombre}','pass': f'{password}'})
    else:
        form = FormCrearUsuario()
    return render(request, 'users/signup.html', {'form': form})

def logout_view(request):
    """Función para cerrar sesión, se encarga de cerrar la sesión del usuario y de redirigir a la pagina de login"""

    logout(request)
    return redirect('users:login')
