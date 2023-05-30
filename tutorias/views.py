from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import Usuario
from .models import Tutoria
from mensajes.models import Mensaje
from .forms import Calendario

@login_required(login_url='users:login')
def tutorias(request):
    """Vista de las tutorias del usuario (representadas por mensajes), muestra las tutorias que ha solicitado, tiene activas
    y en el caso de ser tutor, las que ha aceptado y las que ha rechazado"""

    chats = Mensaje.getMensajes(usuario=request.user)
    chatActivo = None
    mensajes = None
	
    if chats:
        chat = chats[0]
        chatActivo = chat['Usuario']
        mensajes = Mensaje.objects.filter(usuario=request.user, receptor=chat['Usuario'], tutoria__id=chat['tutoria'].id)
        mensajes.update(leido=True)
        tutoriaActiva = chat['tutoria']
        for chat in chats:
            if chat['Usuario'] == chatActivo:
                chat['sinleer'] = 0
                
    return render(request, 'tutorias.html', {
        'mensajes': mensajes,
		'chats': chats,
		'chatActivo': chatActivo,
        'tutoriaActiva': tutoriaActiva,
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

        tutoria = Tutoria.objects.create(nombre=request.POST["Nombre"],tema=request.POST["Tema"],tutor=tutor, usuario=estudiante)
        return redirect('nuevaConversacion', emailtutor, tutoria.id)

@login_required(login_url='users:login')
def agendar(request, tutoria_id):
    """Vista para agendar la tutoria en google calendar"""

    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    if request.method == "POST":
        form = Calendario(request.POST, instance=tutoria)#, request.FILES, instance=tutoria)
        if form.is_valid():
            form.save()
            tutoria.addCalendario()
            return redirect('tutorias')
    else:
        form = Calendario(instance=tutoria)
        return render(request, 'detalleTutoria.html', {
            'form': form,
            'tutoria': tutoria,
        })

@login_required(login_url='users:login')
def aceptar_tutoria(request, tutoria_id):
    """Vista para aceptar una tutoria"""

    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    tutoria.estado='Aceptada'
    tutoria.save()
    return redirect('tutorias')

@login_required(login_url='users:login')
def rechazar_tutoria(request, tutoria_id):
    """Vista para rechazar una tutoria"""

    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    tutoria.estado='Rechazada'
    tutoria.save()
    return redirect('tutorias')

@login_required(login_url='users:login')
def eliminar_tutoria(request, tutoria_id):
    """Vista para eliminar una tutoria"""

    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    tutoria.delete()
    return redirect('tutorias')
    

