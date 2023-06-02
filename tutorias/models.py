from django.db import models
from django.conf import settings
import uuid #para crear id unicos, y que sirvan a la hora de migrar la base de datos, si lo vemos necesario.

# Librerias para el calendario
import os.path
import datetime
import pickle
from datetime import timedelta
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Create your models here.


class Tutoria(models.Model):
    """Modelo para las tutorias que representa su estructura en la base de datos"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=200)
    tema = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=False, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    lugar = models.CharField(max_length=200, default="Biblioteca")
    estado = models.CharField(max_length=200, default="Solicitada")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="usuario_tutorias")
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tutor_tutorias")

    def __str__(self):
        """Devuelve el nombre de la tutoria junto a su tema"""
        return "Tutoria: " + self.nombre + ". (" + self.tema + ")"
    
    def addCalendario(self):
        """Agrega la tutoria al calendario"""
        
        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/calendar']

        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        start_time = self.fecha
        end_time= start_time + timedelta(minutes=120)
        
        try:
            service = build('calendar', 'v3', credentials=creds)

            event = (
                service.events()
                .insert(
                    calendarId="primary",
                    body={
                        "summary": self.nombre,
                        "description": self.tema,
                        "location": self.lugar,
                        "start": {"dateTime": start_time.isoformat(),
                        'timeZone': 'America/Bogota',                        
                        },
                        "end": {
                            "dateTime": end_time.isoformat(),
                            'timeZone': 'America/Bogota',
                        },
                        "attendees":[{"email":self.usuario.email}]
                    },
                ).execute()
            )
            return "Tutoria agregada al calendario %s" % event.get("htmlLink")
        except HttpError as err:
            return 'Algo ha ido mal: %s' % err