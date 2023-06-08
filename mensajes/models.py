from django.db import models
from users.models import Usuario
from tutorias.models import Tutoria
from django.db.models import Max

# Create your models here.
class Mensaje(models.Model):
	# Usuario al que se le adjudican los mensajes, para finalidad de filtrado
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='Usuario')

	emisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emisor')
	receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='receptor')
	cuerpo = models.TextField(max_length=1000, blank=True, null=True)
	fecha = models.DateTimeField(auto_now_add=True)
	# indica si el mensaje ha sido leido por el receptor
	leido = models.BooleanField(default=False)
	# Tutoria a la que pertenece el mensaje
	tutoria = models.ForeignKey(Tutoria, on_delete=models.CASCADE, related_name='tutoria', blank=True, null=True)
	
	def enviarMensaje(emisor, receptor, cuerpo, tutoria):
		"""Metodo para crear los mensajes de ambas partes de la conversacion"""

		# Se crea el mensaje para el emisor
		emisorMensaje = Mensaje(
			usuario=emisor,
			emisor=emisor,
			receptor=receptor,
			cuerpo=cuerpo,
			tutoria=tutoria,
			leido=True)
		emisorMensaje.save()

		# Se crea el mensaje para el receptor
		receptorMensaje = Mensaje(
			usuario=receptor,
			emisor=emisor,
			cuerpo=cuerpo,
			receptor=emisor,
			tutoria=tutoria)
		receptorMensaje.save()
		return emisorMensaje

	def getMensajes(usuario):
		"""Metodo para obtener los mensajes de un usuario"""

		# Se obtienen los mensajes del usuario agrupados por chats y se ordenan por fecha
		chats = Mensaje.objects.filter(usuario=usuario).values('receptor','tutoria').annotate(last=Max('fecha')).order_by('-last')
		
		usuarios = []
		for chat in chats:
			usuarios.append({
				# Se obtiene el usuario receptor del chat
				'Usuario': Usuario.objects.get(pk=chat['receptor']),
				# Se obtiene el ultimo mensaje del chat
				'ultimo': chat['last'],
				# Se obtiene el numero de mensajes sin leer del chat
				'sinleer': Mensaje.objects.filter(usuario=usuario, receptor__pk=chat['receptor'], leido=False).count(),
				# Se obtiene la tutoria del chat
				'tutoria': Tutoria.objects.get(pk=chat['tutoria'])
			})
			
		return usuarios