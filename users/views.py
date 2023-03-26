from django.contrib.auth import authenticate, get_user_model, login, logout # Para autenticar, crear usuarios y cerrar sesión
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password # Para encriptar la contraseña
from django.http.response import HttpResponse, JsonResponse

def user_login(request):
    """Funcion para iniciar sesion, se encarga de autenticar al usuario y de redirigirlo a la pagina principal
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

def user_singup(request):
    """Funcion para crear un nuevo usuario y de redirigirlo a la pagina principal una vez registrado
    En caso de que el usuario ya exista o alguna credencial sea invalida, se muestra un mensaje de error"""
    
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['Nombre']
        password = request.POST['password']
        user = authenticate(request, username=username, nombre=name, password=password)
        try:
            user = get_user_model().objects.create(
                email=username,
                nombre=name,
                password=make_password(password),
                is_active=True
            )
            login(request, user)
            return redirect('core:home')

        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})
    return render(request, 'users/singup.html')

def logout_view(request):
    """Funcion para cerrar sesion, se encarga de cerrar la sesion del usuario y de redirigirlo a la pagina de login"""

    logout(request)
    return redirect('users:login')
