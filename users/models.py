from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
from django.urls import reverse
from django.utils.text import slugify  #para crear urls únicas y legibles, identificación del usuario
import uuid #para crear id únicos, y que sirvan a la hora de migrar la base de datos, si lo vemos necesario.
import random
import string

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

class CustomAccountManager(BaseUserManager):
    """'Custom account model manager', se encarga de crear los usuarios ya sea los normales o los super usuarios
    se hizo de esta manera para utilizar mas eficientemente las herramientas de Django."""

    def create_user(self, email, nombre, password, **other_fields):
        """Crea y guarda un nuevo usuario normal"""

        if not email:
            raise ValueError('Se debe ingresar un email')

        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, nombre, password, **other_fields):
        """Crea y guarda un nuevo super usuario"""

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
    """Modelo de usuario, se hereda de AbstractUser, que es el modelo de usuario de Django, 
    se le agregan ademas los atributos propios del contexto de la app, como el nombre, 
    el celular, la calificación, si es tutor, etc."""
    
    # variables propias de usuario/estudiante
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    celular = models.CharField(max_length=20, blank=True, null=True)
    calificacion = models.FloatField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)

    # variables propias de django
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # variables propias de tutores
    is_tutor = models.BooleanField(default=False)
    tags = TaggableManager(through=UUIDTaggedItem, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        """Devuelve el nombre del usuario junto con su email"""

        return self.nombre + ", (" + self.email + ")"
    
    def listarTutores(request):
        """Devuelve una lista de todos los tutores registrados en la plataforma
        que equivalen a las posibles tutorías que se pueden contratar"""
        
        tutores = Usuario.objects.filter(is_tutor = True)
        return tutores

    def save(self, *args, **kwargs):
        """Crea un slug único para cada usuario, para que su perfil sea identificable
        antes de guardar el usuario en la base de datos a traves del constructor save"""
        
        if not self.username:
            self.username = self.email

        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.email)
        super(Usuario, self).save(*args, **kwargs)

    #cuando este lista la vista del perfil del usuario, des comentar esto y corregir ruta de la vista
    #def get_absolute_url(self):
    #    return reverse('users:user_detail', args=[self.slug])