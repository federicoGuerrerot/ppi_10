# en views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Favorito
from users.models import Usuario

def favoritos(request):
    """Muestra los favoritos de un usuario"""

    favoritos = Favorito.listarFavoritos(request.user)

    return render(request, 'favoritos/favoritos.html', {	
        'favoritos':favoritos,
        })

def añadirFavorito(request, emailtutor):
    """Añade un favorito"""

    tutor = get_object_or_404(Usuario, email = emailtutor)
    favorito = Favorito(tutor=tutor, usuario=request.user)
    favorito.save()

    return redirect('favoritos')

def eliminarFavorito(request, emailtutor):
    """Elimina un favorito"""

    tutor = get_object_or_404(Usuario, email = emailtutor)
    favorito = Favorito.objects.get(tutor=tutor, usuario=request.user)
    favorito.delete()

    return redirect('favoritos')