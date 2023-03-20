from django.db import models
from users import models as userModel

# Create your models here.
class Tutoria(models.Model):
    Nombre = models.CharField(max_length=200)
    Tema = models.CharField(max_length=200)
    Fecha = models.DateField
    Tarifa = models.IntegerField
    Estado = models.CharField(max_length=200)
    usuario = models.ForeignKey('users.usuario', on_delete=models.CASCADE, related_name="usuario_tutorias")
    tutor = models.ForeignKey('users.usuario', on_delete=models.CASCADE, related_name="tutor_tutorias")
    
    def __str__(self):
        return self.Nombre