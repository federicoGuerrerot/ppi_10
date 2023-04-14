from django import forms
from users.models import Usuario

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'celular', 'descripcion', 'foto_perfil','is_tutor' , 'tags', 'tarifa')
