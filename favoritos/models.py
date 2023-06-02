from django.db import models
from django.conf import settings
import uuid


# Create your models here.
class Favorito(models.Model):
    """Modelo para los favoritos que representa su estructura en la base de datos"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tutor_favoritos")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="usuario_favoritos")

    def añadirFavorito(usuario, tutor):
        """Añade un favorito"""

        favorito = Favorito(tutor=tutor, usuario=usuario)
        favorito.save()
        return favorito
    
    def eliminarFavorito(usuario, tutor):
        """Elimina un favorito"""

        favorito = Favorito.objects.get(tutor=tutor, usuario=usuario)
        favorito.delete()
        return favorito
    
    def listarFavoritos(usuario):
        """Lista todos los favoritos de un usuario"""

        favoritos = Favorito.objects.filter(usuario=usuario)
        return favoritos