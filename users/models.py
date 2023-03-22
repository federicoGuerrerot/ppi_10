from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import uuid #para crear id unicos, y que sirvan a la hora de migrar la base de datos, si lo vemos necesario.
import random
import string

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, nombre, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, nombre, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, nombre, password, **other_fields)


class Usuario(AbstractUser):
    #Usuario de la app "hereda" del custos AccountManager, ese es el que se encarga de crear los usuarios ya sea los normales o los superusuarios
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    celular = models.CharField(max_length=20, blank=True, null=True)
    calificacion = models.FloatField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    #para urls unicas, identificacion del usuario

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

    # falta definir variables propias de tutores

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.nombre
    
    def get_email(self):
        return self.email
    
    def listarTutores(request):
        tutores = Usuario.objects.filter(is_tutor = True)
        return tutores
    
    #cuando este lista la vista del perfil del usuario, descomentar esto y corregir ruta de la vista
    #def get_absolute_url(self):
    #    return reverse('users:user_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.email)
        super(Usuario, self).save(*args, **kwargs)
