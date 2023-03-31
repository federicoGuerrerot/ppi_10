from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect
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

def tutor(request, tutorslug):
    """Vista de un tutor en particular, muestra los datos del tutor"""

    if request.method == 'GET':
        tutor = get_object_or_404(Usuario, slug=tutorslug)
        return render(request, 'core/tutor.html', {'tutor':tutor})
    else:
        return render(request, 'tutorias/solicitarTutoria.html', {'tutor' : tutor}) ## no sirve

def buscar(request, slug):
    """Vista de busqueda de tutores, muestra los tutores que coinciden
    se hace uso de la libreria taggit para la busqueda de tags (Temas)"""

    tag = get_object_or_404(Tag, slug=slug)
    populares = Usuario.tags.most_common()[:5]
    tutores = Usuario.objects.filter(tags=tag)
    return render(request, 'core/home.html', {
        'populares':populares,
        'tutores':tutores, 
    })

def buscarbarra(request):
    """Metodo de busqueda editado para que funcione la barra de busqueda
    mediante un form GET"""

    slug = request.GET['buscar'].lower()
    tag = get_object_or_404(Tag, slug=slug)
    if tag:
        populares = Usuario.tags.most_common()[:5]
        tutores = Usuario.objects.filter(tags=tag)
        return render(request, 'core/home.html', {
            'populares':populares,
            'tutores':tutores, 
        })
    else:
        messages.error(request, 'No se encontraron resultados')
    
