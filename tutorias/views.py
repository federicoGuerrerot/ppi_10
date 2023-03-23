from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required # Para requerir que el usuario esté autenticado
from users.models import Usuario
from .models import Tutoria
from .forms import SolicitaNuevaTutoria

# Create your views here.
@login_required(login_url='users:login')
def tutorias(request): #########################falta agregar boton para ver las tutorias activas del usuario
    listatutorias = Tutoria.objects.filter(usuario = request.user)
    return render(request, 'tutorias.html', {
        'listatutorias' : listatutorias,
    })

@login_required(login_url='users:login')
def detalle_tutoria(request, tutoria_id):
    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    return render(request, 'detalleTutoria.html', {
        'tutoria':tutoria,
    })

@login_required(login_url='users:login')
def solicitarTutoria(request, emailtutor):
    tutor = get_object_or_404(Usuario, email = emailtutor)
    if request.method == 'GET':
        return render(request, 'solicitarTutoria.html', {
            #'form': SolicitaNuevaTutoria()
            'tutor': tutor,
        })
    else:
        estudiante = request.user
        Tutoria.objects.create(Nombre=request.POST["Nombre"],Tema=request.POST["Tema"],tutor=tutor, usuario=estudiante)
        return redirect('tutorias',estudiante.id)

@login_required(login_url='users:login')
def eliminar_tutoria(request): #falta
    if request.method == 'GET':
        return render(request, 'solicitarTutoria.html', {
            'form': SolicitaNuevaTutoria()
        })
    else:
        Tutoria.objects.create(Nombre=request.POST["Nombre"],Tema=request.POST["Tema"],Usuarioemail = 'admintutor@unal.edu.co')
        return redirect('tutorias')
    

