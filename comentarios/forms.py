from django import forms
from .models import Comentario

class ActualizarComentario(forms.ModelForm):
    """Formulario para actualizar un comentario"""

    calificacion = forms.IntegerField(label="Calificacion", required=True)
    comentario = forms.CharField(label="Cuentanos tu experiencia", required=True)

    class Meta:
        model = Comentario
        fields = ('calificacion', 'comentario')