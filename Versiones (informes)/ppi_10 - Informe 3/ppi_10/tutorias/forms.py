from django import forms

class SolicitaNuevaTutoria(forms.Form):
    """Formulario para solicitar una nueva tutoria"""

    nombre = forms.CharField(label="Nombre de la tutoria", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    tema =forms.CharField(label="Tema de la tutoria", widget=forms.Textarea(attrs={'class': 'input'}))
    tutor = forms.CharField(label="Tutor", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    usuario = forms.CharField(label="Usuario", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    fecha = forms.DateField(label="Fecha", widget=forms.TextInput(attrs={'class': 'input'}))
    hora = forms.TimeField(label="Hora", widget=forms.TextInput(attrs={'class': 'input'}))
    duracion = forms.IntegerField(label="Duracion", widget=forms.TextInput(attrs={'class': 'input'}))
    lugar = forms.CharField(label="Lugar", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    tarifa = forms.IntegerField(label="Tarifa", widget=forms.TextInput(attrs={'class': 'input'}))
    estado = forms.CharField(label="Estado", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))