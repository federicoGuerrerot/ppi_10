import uuid

from django.db import models
from django.conf import settings



# Create your models here.

class Comentario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    titular = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="titular")
    emisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="emisor")
    estado = models.CharField(max_length=10, default='Creado') 
    calificacion = models.IntegerField()
    comentario = models.TextField(null=True)

    def crearComentario(emisor, titular):
        """Crea los dos comentarios de la tutoria"""
       
        # Creamos el comentario del emisor
        comentarioEmisor = Comentario(
            titular=titular,
            emisor=emisor,
            calificacion=0,
            comentario=None)
        comentarioEmisor.save()

        # Creamos el comentario del titular
        comentarioTitular = Comentario(
            titular=emisor,
            emisor=titular,
            calificacion=0,
            comentario=None)
        comentarioTitular.save()

        return comentarioEmisor

    def actualizarCalificacion(self):
        """Actualiza la calificacion del usuario titular"""
        
        # Obtenemos todos los comentarios del titular
        comentarios = Comentario.objects.filter(titular=self.titular, estado='Publicado')
        
        # Calculamos la nueva calificacion
        suma = 0
        for comentario in comentarios:
            suma += comentario.calificacion
        self.titular.calificacion = suma/len(comentarios)
        self.titular.save()

