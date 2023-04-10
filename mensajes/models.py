from django.db import models
from users.models import Usuario
from django.db.models import Max

# Create your models here.
class mensaje(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='Usuario')
	emisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emisor')
	receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='receptor')
	cuerpo = models.TextField(max_length=1000, blank=True, null=True)
	fecha = models.DateTimeField(auto_now_add=True)
	leido = models.BooleanField(default=False)

	def enviarMensaje(emisor, receptor, cuerpo):
		emisorMensaje = mensaje(
			usuario=emisor,
			emisor=emisor,
			receptor=receptor,
			cuerpo=cuerpo,
			leido=True)
		emisorMensaje.save()

		receptorMensaje = mensaje(
			usuario=receptor,
			emisor=emisor,
			cuerpo=cuerpo,
			receptor=emisor,)
		receptorMensaje.save()
		return emisorMensaje

	def get_messages(Usuario):
		mensajes = mensaje.objects.filter(usuario=Usuario).values('receptor').annotate(last=Max('fecha')).order_by('-last')
		users = []
		for mensaje in mensajes:
			users.append({
				'Usuario': Usuario.objects.get(pk=mensaje['receptor']),
				'last': mensaje['last'],
				'unread': mensaje.objects.filter(usuario=Usuario, recipient__pk=mensaje['receptor'], leido=False).count()
				})
		return users