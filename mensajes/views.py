from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from django.contrib.auth.decorators import login_required

from users.models import Usuario
from .models import Mensaje
from tutorias.models import Tutoria

# Create your views here.

@login_required
def directs(request, email, tutoria_id):
	"""Vista para ver los chats de una conversacion"""

	usuario = request.user
	chats = Mensaje.getMensajes(usuario=usuario)
	chatActivo = Usuario.objects.get(email=email)
	mensajes = Mensaje.objects.filter(usuario=usuario, receptor__email=email, tutoria__id=tutoria_id)
	mensajes.update(leido=True)
	tutoriaActiva = Tutoria.objects.get(id=tutoria_id)
	for chat in chats:
		if chat['Usuario'] == chatActivo:
			chat['sinleer'] = 0

	context = {
		'mensajes': mensajes,
		'chats': chats,
		'chatActivo':chatActivo,
		'tutoriaActiva': tutoriaActiva,
	}

	return render(request, 'tutorias.html', context)


@login_required
def nuevaConversacion(request, email, tutoria_id):
	"""Crea una nueva conversacion con el tutor, enviando un mensaje
	por defecto de solicitud de tutoria"""

	emisor = request.user
	cuerpo = 'Hola, estoy interesado en una tutoria, que horario hay disponible?.'
	tutoria = Tutoria.objects.get(id=tutoria_id)
	receptor = Usuario.objects.get(email=email)

	if emisor != receptor:
		Mensaje.enviarMensaje(emisor, receptor, cuerpo, tutoria)
	return redirect('tutorias')

@login_required
def enviar(request):
	"""Envia un mensaje a un usuario"""

	emisor = request.user
	receptor_username = request.POST.get('receptor')
	cuerpo = request.POST.get('cuerpo')
	tutoria = request.POST.get('tutoria')
	
	if request.method == 'POST':
		receptor = Usuario.objects.get(username=receptor_username)
		tutoria = Tutoria.objects.get(id=tutoria)
		Mensaje.enviarMensaje(emisor, receptor, cuerpo, tutoria)
		return redirect('tutorias')
	else:
		HttpResponseBadRequest()

def checkChats(request):
	"""Comprueba si hay chats sin leer"""

	mensajes_count = 0
	if request.user.is_authenticated:
		mensajes_count = Mensaje.objects.filter(usuario=request.user, leido=False).count()

	return {'mensajes_count':mensajes_count}