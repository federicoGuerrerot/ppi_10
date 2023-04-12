from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import Usuario
from .models import Tutoria
from .forms import SolicitaNuevaTutoria
from mensajes.models import Mensaje

@login_required(login_url='users:login')
def tutorias(request):
    """Vista de las tutorias del usuario, muestra las tutorias que ha solicitado, tiene activas
    y en el caso de ser tutor, las que ha aceptado y las que ha rechazado"""

    listatutorias = Tutoria.objects.filter(usuario = request.user)
    mensajes = Mensaje.getMensajes(usuario=request.user)
    chatActivo = None
    chats = None
	
    if mensajes:
        mensaje = mensajes[0]
        chatActivo = mensaje['Usuario'].username
        chats = Mensaje.objects.filter(usuario=request.user, receptor=mensaje['Usuario'])
        chats.update(leido=True)
        for mensaje in mensajes:
            if mensaje['Usuario'].username == chatActivo:
                mensaje['unread'] = 0
                
    return render(request, 'tutorias.html', {
        'chats': chats,
		'mensajes': mensajes,
		'chatActivo': chatActivo,
        'listatutorias' : listatutorias,
    })

@login_required(login_url='users:login')
def detalle_tutoria(request, tutoria_id):
    """Vista de la tutoria seleccionada, muestra los detalles de la tutoria"""

    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    return render(request, 'detalleTutoria.html', {
        'tutoria':tutoria,
    })

@login_required(login_url='users:login')
def solicitarTutoria(request, emailtutor):
    """Vista para solicitar una nueva tutoria"""

    tutor = get_object_or_404(Usuario, email = emailtutor)
    if request.method == 'GET':
        return render(request, 'solicitarTutoria.html', {
            #'form': SolicitaNuevaTutoria()
            'tutor': tutor,
        })
    else:
        estudiante = request.user
        #if form.is_valid():
            #new_tutoria = form.save(commit=False)
            #form.save_m2m()
        #### ejemplo para seguir con usuario, para tutoria es solo: new_tutoria = form.save().

        Tutoria.objects.create(nombre=request.POST["Nombre"],tema=request.POST["Tema"],tutor=tutor, usuario=estudiante)
        return redirect('tutorias')

@login_required(login_url='users:login')
def eliminar_tutoria(request, tutoria_id):
    """Vista para eliminar una tutoria"""

    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    tutoria.delete()
    return redirect('tutorias')
    

