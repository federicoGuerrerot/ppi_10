from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

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
