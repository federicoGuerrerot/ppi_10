from django.shortcuts import render
from users.models import Usuario

def home(request):
    # requerir lista de tutores
    tutores = Usuario.listarTutores(request)
    return render(request, 'core/home.html',{
        'tutores':tutores,
    })
