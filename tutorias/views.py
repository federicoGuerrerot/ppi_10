from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import Usuario
from .models import Tutoria
from mensajes.models import Mensaje
from .forms import Calendario

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

@login_required(login_url='users:login')
def tuto(request):
    """Vista de las tutorias del usuario (representadas por mensajes), muestra las tutorias que ha solicitado, tiene activas
    y en el caso de ser tutor, las que ha aceptado y las que ha rechazado"""
        
    chats = Mensaje.getMensajes(usuario=request.user)
    chatActivo = None
    mensajes = None
	
    if chats:
        chat = chats[0]
        chatActivo = chat['Usuario']
        mensajes = Mensaje.objects.filter(usuario=request.user, receptor=chat['Usuario'], tutoria__id=chat['tutoria'].id)
        mensajes.update(leido=True)
        tutoriaActiva = chat['tutoria']
        for chat in chats:
            if chat['Usuario'] == chatActivo:
                chat['sinleer'] = 0
                
    return render(request, 'tuto.html', {
        'mensajes': mensajes,
		'chats': chats,
		'chatActivo': chatActivo,
        'tutoriaActiva': tutoriaActiva,
    })

@login_required(login_url='users:login')
def tutorias(request):
    """Vista de las tutorias del usuario (representadas por mensajes), muestra las tutorias que ha solicitado, tiene activas
    y en el caso de ser tutor, las que ha aceptado y las que ha rechazado"""
        
    chats = Mensaje.getMensajes(usuario=request.user)
    chatActivo = None
    mensajes = None
	
    if chats:
        chat = chats[0]
        chatActivo = chat['Usuario']
        mensajes = Mensaje.objects.filter(usuario=request.user, receptor=chat['Usuario'], tutoria__id=chat['tutoria'].id)
        mensajes.update(leido=True)
        tutoriaActiva = chat['tutoria']
        for chat in chats:
            if chat['Usuario'] == chatActivo:
                chat['sinleer'] = 0
                
    return render(request, 'tutorias.html', {
        'mensajes': mensajes,
		'chats': chats,
		'chatActivo': chatActivo,
        'tutoriaActiva': tutoriaActiva,
    })

@login_required(login_url='users:login')
def detalle_tutoria(request, tutoria_id):
    """Vista de la tutoria seleccionada, muestra los detalles de la tutoria"""

    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    return render(request, 'detalleTutoria.html', {
        'tutoria':tutoria,
    })

@login_required(login_url='users:login')
def solicitarTutoria(request, emailtutor):
    """Vista para solicitar una nueva tutoria"""

    tutor = get_object_or_404(Usuario, email = emailtutor)
    if request.method == 'GET':
        return render(request, 'solicitarTutoria.html', {
            #'form': SolicitaNuevaTutoria()
            'tutor': tutor,
        })
    else:
        estudiante = request.user
        #if form.is_valid():
            #new_tutoria = form.save(commit=False)
            #form.save_m2m()
        #### ejemplo para seguir con usuario, para tutoria es solo: new_tutoria = form.save().

        tutoria = Tutoria.objects.create(nombre=request.POST["Nombre"],tema=request.POST["Tema"],tutor=tutor, usuario=estudiante)
        return redirect('nuevaConversacion', emailtutor, tutoria.id)

@login_required(login_url='users:login')
def agendar(request, tutoria_id):
    """Vista para agendar la tutoria en google calendar"""

    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    if request.method == "POST":
        form = Calendario(request.POST, instance=tutoria)#, request.FILES, instance=tutoria)
        if form.is_valid():
            form.save()
            creds = Credentials(**request.session['credentials'])
            tutoria.addCalendario(creds)
            return redirect('tutorias')
    else:
        form = Calendario(instance=tutoria)
        return render(request, 'detalleTutoria.html', {
            'form': form,
            'tutoria': tutoria,
        })

@login_required(login_url='users:login')
def aceptar_tutoria(request, tutoria_id):
    """Vista para aceptar una tutoria"""

    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    tutoria.estado='Aceptada'
    tutoria.save()
    return redirect('tutorias')

@login_required(login_url='users:login')
def rechazar_tutoria(request, tutoria_id):
    """Vista para rechazar una tutoria"""

    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    tutoria.estado='Rechazada'
    tutoria.save()
    return redirect('tutorias')

@login_required(login_url='users:login')
def eliminar_tutoria(request, tutoria_id):
    """Vista para eliminar una tutoria"""

    tutoria = get_object_or_404(Tutoria, id = tutoria_id)
    tutoria.delete()
    return redirect('tutorias')
    
    # Pasos API
    # 1. Verificar si existen las credenciales
    # 2. Si no existen, crearlas y guardarlas en la sesion
    # Para crear las credenciales se redirecciona a la vista de autorizacion de Google "authorization_url"
    # 3. Si existen, se redirecciona a agendar y se ejecuta la funcion addCalendario() de la clase Tutoria
    # 4. Redireccionar a la vista de tutorias

@login_required(login_url='users:login')
def test_api(request, tutoria_id):
    """Realiza la verificacion de credenciales para la API de Google Calendar, si no existen las credenciales, procede a crearlas.
    Si existen las credenciales, las carga y ejecuta la funcion addCalendario() de la clase Tutoria y redirecciona a la vista de tutorias"""

    SCOPES = ['https://www.googleapis.com/auth/calendar']
    if 'credentials' not in request.session:

        flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
        flow.redirect_uri = 'http://127.0.0.1:8000/test_api2'

        authorization_url, state = flow.authorization_url(
            # Enable offline access so that you can refresh an access token without
            # re-prompting the user for permission. Recommended for web server apps.
            access_type='offline',
            # Enable incremental authorization. Recommended as a best practice.
            include_granted_scopes='true')

        request.session['state'] = state

        return redirect(authorization_url)

    return redirect('agendar', tutoria_id)

def test_api2(request):
    """Vista para obtener las credenciales de la API de Google Calendar"""

    SCOPES = ['https://www.googleapis.com/auth/calendar']    
    
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES, state=request.session['state'])
    flow.redirect_uri = 'http://127.0.0.1:8000/test_api2'

    # Verifica las credenciales
    flow.fetch_token(authorization_response=request.build_absolute_uri().replace('http', 'https'))
    
    creds = flow.credentials
    # refresca las credenciales por si estas se han actualizado
    request.session['credentials'] = {'token': creds.token,
                                    'refresh_token': creds.refresh_token,
                                    'token_uri': creds.token_uri,
                                    'client_id': creds.client_id,
                                    'client_secret': creds.client_secret,
                                    'scopes': creds.scopes}
    
    return redirect('tutorias')