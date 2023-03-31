from django.shortcuts import render, redirect
from .forms import PerfilForm
from users.models import Usuario

def mi_perfil(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfiles:mi_perfil')
    else:
        form = PerfilForm(instance=request.user)
    return render(request, 'perfiles/mi_perfil.html', {'form': form})
