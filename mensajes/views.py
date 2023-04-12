from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from django.contrib.auth.decorators import login_required

from users.models import Usuario
from .models import Mensaje

from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

@login_required
def Inbox(request):
	"""Vista de la bandeja de entrada del usuario"""

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

	context = {
		'chats': chats,
		'mensajes': mensajes,
		'chatActivo': chatActivo,
		}

	return render(request, 'inbox.html', context)

@login_required
def buscarUsuario(request):
	"""Vista para buscar conversaciones con el tutor"""

	query = request.GET.get("q")
	context = {}
	
	if query:
		usuarios = Usuario.objects.filter(Q(username__icontains=query))

		#Pagination
		paginator = Paginator(usuarios, 6)
		page_number = request.GET.get('page')
		users_paginator = paginator.get_page(page_number)

		context = {
				'usuarios': users_paginator,
			}
	
	return render(request, 'buscarUsuario.html', context)

@login_required
def directs(request, email):
	"""Vista para ver los mensajes de una conversacion"""

	usuario = request.user
	mensajes = Mensaje.getMensajes(usuario=usuario)
	chatActivo = email
	chats = Mensaje.objects.filter(usuario=usuario, receptor__email=email)
	chats.update(leido=True)
	for mensaje in mensajes:
		if mensaje['Usuario'].email == email:
			mensaje['unread'] = 0

	context = {
		'chats': chats,
		'mensajes': mensajes,
		'chatActivo':chatActivo,
	}

	return render(request, 'inbox.html', context)


@login_required
def nuevaConversacion(request, email):
	"""Crea una nueva conversacion con el tutor, enviando un mensaje
	por defecto de solicitud de tutoria"""

	emisor = request.user
	cuerpo = 'Hola, estoy interesado en una tutoria, que horario hay disponible?.'
	try:
		receptor = Usuario.objects.get(email=email)
	except Exception as e:
		return redirect('buscarUsuario')
	if emisor != receptor:
		Mensaje.enviarMensaje(emisor, receptor, cuerpo)
	return redirect('inbox')

@login_required
def enviar(request):
	"""Envia un mensaje a un usuario"""

	emisor = request.user
	receptor_username = request.POST.get('receptor')
	cuerpo = request.POST.get('cuerpo')
	
	if request.method == 'POST':
		receptor = Usuario.objects.get(username=receptor_username)
		Mensaje.enviarMensaje(emisor, receptor, cuerpo)
		return redirect('inbox')
	else:
		HttpResponseBadRequest()

def checkChats(request):
	"""Comprueba si hay mensajes sin leer"""

	chats_count = 0
	if request.user.is_authenticated:
		chats_count = Mensaje.objects.filter(usuario=request.user, leido=False).count()

	return {'chats_count':chats_count}