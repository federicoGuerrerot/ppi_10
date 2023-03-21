from django.shortcuts import render, redirect, get_object_or_404
from users.models import Usuario
from .models import Tutoria
from .forms import CreaNuevaTutoria

# Create your views here.
def tutorias(request, id):
    listatutorias = Tutoria.objects.filter(usuario_id = id)
    return render(request, 'tutorias.html', {
        'listatutorias' : listatutorias,
    })

def detalle_tutoria(request, tutoria_id):
    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    return render(request, 'detalleTutoria.html', {
        'tutoria':tutoria,
    })

def crear_tutoria(request):
    if request.method == 'GET':
        return render(request, 'crearTutoria.html', {
            'form': CreaNuevaTutoria()
        })
    else:
        Tutoria.objects.create(Nombre=request.POST["Nombre"],Tema=request.POST["Tema"],tutor=get_object_or_404(Usuario, id = 1), usuario=get_object_or_404(Usuario, id = 2))
        return redirect('tutorias',2)

def eliminar_tutoria(request): #falta
    if request.method == 'GET':
        return render(request, 'crearTutoria.html', {
            'form': CreaNuevaTutoria()
        })
    else:
        Tutoria.objects.create(Nombre=request.POST["Nombre"],Tema=request.POST["Tema"],Usuarioemail = 'admintutor@unal.edu.co')
        return redirect('tutorias')
    

