from django.db import models

# Create your models here.
class Usuario(models.Model):
    Nombre = models.CharField(max_length=200)
    Correo = models.CharField(max_length=200)
    Contraseña = models.CharField(max_length=200)
    Celular = models.IntegerField
    Comentarios = models.CharField(max_length=200)
    Calificacion = models.IntegerField
    Descripcion = models.CharField(max_length=1000)
    TemasConocimiento = models.CharField(max_length=1000)

    def __str__(self):
        return self.Nombre