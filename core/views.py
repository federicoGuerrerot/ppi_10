from django.shortcuts import render, get_object_or_404
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


def tutor(request, slug):
    """Vista de un tutor en particular, muestra los datos del tutor"""

    tutor = get_object_or_404(Usuario, slug=slug)
    return render(request, 'core/tutor.html', {'tutor':tutor})

def buscar(request, slug):
    """Vista de busqueda de tutores, muestra los tutores que coinciden
    se hace uso de la libreria taggit para la busqueda de tags (Temas)"""

    tag = get_object_or_404(Tag, slug=slug)
    tutores = Usuario.objects.filter(tags=tag)
    return render(request, 'core/buscar.html', {'tutores':tutores, 'tag':tag})