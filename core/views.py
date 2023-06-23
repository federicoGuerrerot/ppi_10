from django.shortcuts import render, get_object_or_404, redirect
from users.models import Usuario
from taggit.models import Tag

def home(request):
    """Vista de la pagina principal, muestra los tutores registrados
    junto con sus tags los cuales representan los temas que imparten
    y la funcion de busqueda de tutores.
    """
    # Recupera la lista de tutores
    tutores = Usuario.listarTutores(request)
    
    # Lista los tags mas populares (5)
    populares = Usuario.tags.most_common()[:5]

    return render(request, 'core/home.html',{
        'tutores':tutores,
        'populares':populares,	
    })

def tutor(request, tutorslug):
    """Vista de un tutor en particular, muestra los datos del tutor y ofrece la opcion para 
    solicitar una tutoria con este."""

    # Recupera el tutor, en la plantilla html se accede a sus datos y se muestran 
    tutor = get_object_or_404(Usuario, slug=tutorslug)
    ya_es_favorito = request.session.get('ya_es_favorito', False)
    return render(request, 'core/tutor.html', {
        'tutor':tutor,
        'ya_es_favorito': ya_es_favorito
    })
    

def buscar(request, slug):
    """Vista de busqueda de tutores, muestra los tutores que coinciden
    se hace uso de la libreria taggit para la busqueda de tags, que en el 
    contexto de este proyecto referencian los temas que imparten los tutores"""

    # Recupera el tag mediante el slug (identificador unico)
    tag = get_object_or_404(Tag, slug=slug)

    # Recupera los tags mas populares (5)
    populares = Usuario.tags.most_common()[:5]

    # Recupera los tutores que imparten el tema del tag
    tutores = Usuario.objects.filter(tags=tag)

    return render(request, 'core/home.html', {
        'populares':populares,
        'tutores':tutores, 
    })

def buscarbarra(request):
    """Metodo de busqueda editado para que funcione la barra de busqueda
    mediante un form GET"""

    # este metodo posee la misma estructura que el metodo buscar
    slug = request.GET['buscar'].lower()
    tag = get_object_or_404(Tag, slug=slug)
    populares = Usuario.tags.most_common()[:5]
    tutores = Usuario.objects.filter(tags=tag)

    return render(request, 'core/home.html', {
        'populares':populares,
        'tutores':tutores, 
    })

def contacto(request):
    """Vista de la pagina de contacto, en donde se muestra la informacion de contacto
    de los desarrolladores del proyecto"""
    
    return render(request, 'core/contacto.html')
