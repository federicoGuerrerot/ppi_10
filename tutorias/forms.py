from django import forms
from .models import Tutoria

class SolicitaNuevaTutoria(forms.Form):
    """Formulario para solicitar una nueva tutoria"""

    class Meta:
        # Modelo en el que se basa el formulario    
        model = Tutoria
        # Campos a integrar en el formulario
        fields = ('nombre', 'tema', 'is_tutor', 'tags')

class Calendario(forms.ModelForm):
    """Formulario para agendar una tutoria en google calendar"""

    # Validaciones a hacer en el formulario
    fecha = forms.DateTimeField(label="startDateTime", input_formats=['%Y/%m/%d %H:%M'], required=True)

    class Meta:
        # Modelo en el que se basa el formulario
        model = Tutoria
        # Campos a integrar en el formulario
        fields = ('nombre', 'tema', 'fecha', 'lugar', 'duracion')