from django import forms
from .models import Comentario

class ActualizarComentario(forms.ModelForm):
    """Formulario para actualizar un comentario"""

    # Agregar restricciones necesarias a los campos
    calificacion = forms.IntegerField(label="Calificacion", required=True)
    comentario = forms.CharField(label="Cuentanos tu experiencia", required=True)

    class Meta:
        # Modelo al que pertenece el formulario
        model = Comentario

        # Campos del modelo que se van a mostrar en el formulario
        fields = ('calificacion', 'comentario')