from django import forms
from .models import Tutoria

class SolicitaNuevaTutoria(forms.Form):
    """Formulario para solicitar una nueva tutoria"""

    class Meta:
        model = Tutoria
        fields = ('nombre', 'tema', 'is_tutor', 'tags')