from django.db import models
from users.models import Usuario
from tutorias.models import Tutoria
from django.db.models import Max

# Create your models here.
class Mensaje(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='Usuario')
	emisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emisor')
	receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='receptor')
	cuerpo = models.TextField(max_length=1000, blank=True, null=True)
	fecha = models.DateTimeField(auto_now_add=True)
	leido = models.BooleanField(default=False)
	tutoria = models.ForeignKey(Tutoria, on_delete=models.CASCADE, related_name='tutoria', blank=True, null=True)
	
	def enviarMensaje(emisor, receptor, cuerpo, tutoria):
		emisorMensaje = Mensaje(
			usuario=emisor,
			emisor=emisor,
			receptor=receptor,
			cuerpo=cuerpo,
			tutoria=tutoria,
			leido=True)
		emisorMensaje.save()

		receptorMensaje = Mensaje(
			usuario=receptor,
			emisor=emisor,
			cuerpo=cuerpo,
			receptor=emisor,
			tutoria=tutoria)
		receptorMensaje.save()
		return emisorMensaje

	def getMensajes(usuario):
		chats = Mensaje.objects.filter(usuario=usuario).values('receptor','tutoria').annotate(last=Max('fecha')).order_by('-last')
		usuarios = []
		for chat in chats:
			usuarios.append({
				'Usuario': Usuario.objects.get(pk=chat['receptor']),
				'last': chat['last'],
				'unread': Mensaje.objects.filter(usuario=usuario, receptor__pk=chat['receptor'], leido=False).count(),
				'tutoria': Tutoria.objects.get(pk=chat['tutoria'])
				})
		return usuarios