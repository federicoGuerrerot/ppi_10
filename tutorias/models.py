from django.db import models
from django.conf import settings
import uuid #para crear id unicos, y que sirvan a la hora de migrar la base de datos, si lo vemos necesario.

# Create your models here.
class Tutoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    Nombre = models.CharField(max_length=200)
    Tema = models.CharField(max_length=200)
    Fecha = models.DateField
    Tarifa = models.IntegerField
    Estado = models.CharField(max_length=200)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="usuario_tutorias")
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tutor_tutorias")

    def __str__(self):
        return self.Nombre