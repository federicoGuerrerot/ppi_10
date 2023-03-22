from django.contrib.auth import authenticate, get_user_model, login, logout # Para autenticar, crear usuarios y cerrar sesión
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password # Para encriptar la contraseña
from django.http.response import HttpResponse, JsonResponse # Para devolver respuestas

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')  # Reemplazar 'core:home' con la vista de la página principal en tu proyecto
        else:
            # Mensaje de error si las credenciales son incorrectas
            return render(request, 'users/login.html', {'error_message': 'Nombre de usuario o contraseña incorrecta'})
    return render(request, 'users/login.html')

def user_singup(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
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
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('core:home')
