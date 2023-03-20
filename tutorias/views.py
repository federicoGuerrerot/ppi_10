from django.shortcuts import render, redirect, get_object_or_404
from users.models import Usuario
from .models import Tutoria
from .forms import CreaNuevaTutoria

# Create your views here.
def tutorias(request, Correo):
    listatutorias = Tutoria.objects.filter(Tutoria, Usuario_Correo = Correo)
    render(request, 'templates/tutorias.html', {
        'listatutorias' : listatutorias,
    })

def ver_tutoria(request, tutoria_id):
    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    render(request, 'templates/vistaTutoria.html', {
        'tutoria':tutoria,
    })

def crear_tutoria(request):
    if request.method == 'GET':
        return render(request, 'templates/crearTutoria.html', {
            'form': CreaNuevaTutoria()
        })
    else:
        Tutoria.objects.create(Nombre=request.POST["Nombre"],Tema=request.POST["Tema"])
        return redirect('tutorias')

def eliminar_tutoria(request): #falta
    if request.method == 'GET':
        return render(request, 'templates/crearTutoria.html', {
            'form': CreaNuevaTutoria()
        })
    else:
        Tutoria.objects.create(Nombre=request.POST["Nombre"],Tema=request.POST["Tema"])
        return redirect('tutorias')
