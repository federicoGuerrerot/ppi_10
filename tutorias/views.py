from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required # Para requerir que el usuario esté autenticado
from users.models import Usuario
from .models import Tutoria
from .forms import SolicitaNuevaTutoria

# Create your views here.
def tutorias(request, email):
    listatutorias = Tutoria.objects.filter(usuario_email = email)
    return render(request, 'tutorias.html', {
        'listatutorias' : listatutorias,
    })

@login_required(login_url='core:home')
def detalle_tutoria(request, tutoria_id):
    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    return render(request, 'detalleTutoria.html', {
        'tutoria':tutoria,
    })

@login_required(login_url='core:home')
def solicitarTutoria(request, emailtutor):
    tutor = get_object_or_404(Usuario, email = emailtutor)
    if request.method == 'GET':
        return render(request, 'solicitarTutoria.html', {
            #'form': SolicitaNuevaTutoria()
            'tutor': tutor,
        })
    else:
        Tutoria.objects.create(Nombre=request.POST["Nombre"],Tema=request.POST["Tema"],tutor=tutor, usuario=get_object_or_404(Usuario, id = 2))
        return redirect('tutorias',2)

@login_required(login_url='core:home')
def eliminar_tutoria(request): #falta
    if request.method == 'GET':
        return render(request, 'solicitarTutoria.html', {
            'form': SolicitaNuevaTutoria()
        })
    else:
        Tutoria.objects.create(Nombre=request.POST["Nombre"],Tema=request.POST["Tema"],Usuarioemail = 'admintutor@unal.edu.co')
        return redirect('tutorias')
    

