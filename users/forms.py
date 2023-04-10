from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import Usuario

class FormCrearUsuario(UserCreationForm):
    """Formulario para crear un nuevo usuario"""

    class Meta:
        model = Usuario
        fields = ('email', 'nombre', 'celular')
