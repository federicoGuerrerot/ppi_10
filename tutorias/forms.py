from django import forms
from .models import Tutoria

class SolicitaNuevaTutoria(forms.Form):
    """Formulario para solicitar una nueva tutoria"""

    class Meta:
        model = Tutoria
        fields = ('nombre', 'tema', 'is_tutor', 'tags')

class Calendario(forms.ModelForm):

    fecha = forms.DateTimeField(label="startDateTime", input_formats=['%Y/%m/%d %H:%M'], required=True)

    class Meta:
        model = Tutoria
        fields = ('nombre', 'tema', 'fecha', 'lugar', 'duracion')