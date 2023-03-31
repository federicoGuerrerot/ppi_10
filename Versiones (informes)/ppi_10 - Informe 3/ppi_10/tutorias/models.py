from django.db import models
from django.conf import settings
import uuid #para crear id unicos, y que sirvan a la hora de migrar la base de datos, si lo vemos necesario.

# Create your models here.


class Tutoria(models.Model):
    """Modelo para las tutorias que representa su estructura en la base de datos"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=200)
    tema = models.CharField(max_length=200)
    fecha = models.DateField
    hora = models.TimeField
    tarifa = models.IntegerField
    duracion = models.IntegerField
    lugar = models.CharField(max_length=200, default="Biblioteca")
    estado = models.CharField(max_length=200, default="Solicitada")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="usuario_tutorias")
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tutor_tutorias")

    def __str__(self):
        """Devuelve el nombre de la tutoria junto a su tema"""
        return "Tutoria: " + self.nombre + ". (" + self.tema + ")"