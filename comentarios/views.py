from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Comentario
from .forms import ActualizarComentario

# Create your views here.

@login_required(login_url='users:login')
def listarcomentarios(request):
    """Vista de los comentarios del usuario"""

    # Recuperamos los comentarios del usuario
    comentarios = Comentario.objects.filter(titular=request.user, estado='Publicado')
    pendientes = Comentario.objects.filter(fuente=request.user, estado='Creado')

    # Mensaje de "error"
    mensaje = None
    if (not comentarios) & (not pendientes):
        mensaje = "Aun no tienes comentarios"

    return render(request, 'comentarios.html', {
        'comentarios':comentarios,
        'pendientes': pendientes,
        'mensaje': mensaje,
    })

@login_required(login_url='users:login')
def calificar(request, comentario_id):
    """Vista para calificar la tutoria"""

    # Recuperamos el comentario
    comentario = Comentario.objects.get(id=comentario_id)

    if request.method == 'POST':

        # Recuperamos info del formulario
        form = ActualizarComentario(request.POST, instance=comentario)
        
        # Guardamos los cambios y actualizamos la calificacion
        if form.is_valid():
            form.save()
            comentario.estado = 'Publicado'
            comentario.save()
            comentario.actualizarCalificacion()
        
            return redirect('comentarios')
    else:
        # creamos el formulario y lo mostramos
        form = ActualizarComentario(instance=comentario)
        return render(request, 'calificar.html', {
            'form': form,
            'comentario': comentario,
        })
