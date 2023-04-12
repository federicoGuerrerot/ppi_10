from django.db import models
from users.models import Usuario
from django.db.models import Max

# Create your models here.
class Mensaje(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='Usuario')
	emisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emisor')
	receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='receptor')
	cuerpo = models.TextField(max_length=1000, blank=True, null=True)
	fecha = models.DateTimeField(auto_now_add=True)
	leido = models.BooleanField(default=False)
	

	def enviarMensaje(emisor, receptor, cuerpo):
		emisorMensaje = Mensaje(
			usuario=emisor,
			emisor=emisor,
			receptor=receptor,
			cuerpo=cuerpo,
			leido=True)
		emisorMensaje.save()

		receptorMensaje = Mensaje(
			usuario=receptor,
			emisor=emisor,
			cuerpo=cuerpo,
			receptor=emisor,)
		receptorMensaje.save()
		return emisorMensaje

	def getMensajes(usuario):
		mensajes = Mensaje.objects.filter(usuario=usuario).values('receptor').annotate(last=Max('fecha')).order_by('-last')
		usuarios = []
		for mensaje in mensajes:
			usuarios.append({
				'Usuario': Usuario.objects.get(pk=mensaje['receptor']),
				'last': mensaje['last'],
				'unread': Mensaje.objects.filter(usuario=usuario, receptor__pk=mensaje['receptor'], leido=False).count()
				})
		return usuarios