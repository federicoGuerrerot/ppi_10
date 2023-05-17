from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import Usuario

class FormCrearUsuario(UserCreationForm):
    """Formulario para crear un nuevo usuario"""
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-input', 'placeholder': 'Email'}))
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Nombre'}))
    # password1 = forms.CharField(required=True, label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control form-input', 'placeholder': 'Contraseña'}))
    # password2 = forms.CharField(required=True, label='Confirma contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control form-input', 'placeholder': 'Confirma tu contraseña'}))

    class Meta:
        model = Usuario
        fields = ('email', 'nombre', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(FormCrearUsuario, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control form-input'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password1'].help_text = """Tu contraseña: \n No puede ser muy similiar a tus otros datos.\n
                Debe contener al menos 8 caracteres.\n
                Debe contener al menos una letra y al menos un número o caracter especial.\n
                No puede ser completamente numerica\n
                """
        self.fields['password2'].widget.attrs['class'] = 'form-control form-input'
        self.fields['password2'].label = 'Cofirma tu contraseña'
        self.fields['password2'].help_text = "Vuelve a escribir tu contraseña para confirmarla"
        
