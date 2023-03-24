from django.shortcuts import render
from users.models import Usuario
from taggit.models import Tag

def home(request):
    # requerir lista de tutores
    tutores = Usuario.listarTutores(request)
    return render(request, 'core/home.html',{
        'tutores':tutores,
    })
