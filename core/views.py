from django.shortcuts import render
from users.models import Usuario
from taggit.models import Tag

def home(request):
    """Vista de la pagina principal, muestra los tutores registrados
    junto con sus tags los cuales representan los temas que imparten
    y la funcion de busqueda de tutores.
    """
    # Lista de tutores
    tutores = Usuario.listarTutores(request)
    # Lista de tags populares (5)
    populares = Usuario.tags.most_common()[:5]

    return render(request, 'core/home.html',{
        'tutores':tutores,
        'populares':populares,	
    })
