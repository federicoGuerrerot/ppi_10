from django import forms

class CreaNuevaTutoria(forms.Form):
    Nombre = forms.CharField(label="Nombre de la tutoria", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    Tema =forms.CharField(label="Tema de la tutoria", widget=forms.Textarea(attrs={'class': 'input'}))