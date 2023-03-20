from django.db import models
from users import models as userModel

# Create your models here.
class Tutoria(models.Model):
    Nombre = models.CharField(max_length=200)
    Tema = models.CharField(max_length=200)
    Fecha = models.DateField
    Tarifa = models.IntegerField
    Estado = models.CharField(max_length=200)
    Tutor = models.ForeignKey(userModel.Usuario, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(userModel.Usuario, on_delete=models.CASCADE)