from django.db import models
from django.conf import settings
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import datetime
from datetime import timedelta
from googleapiclient.discovery import build
import uuid #para crear id unicos, y que sirvan a la hora de migrar la base de datos, si lo vemos necesario.

# Create your models here.


class Tutoria(models.Model):
    """Modelo para las tutorias que representa su estructura en la base de datos"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre = models.CharField(max_length=200)
    tema = models.CharField(max_length=200)
    fecha = models.DateField
    hora = models.TimeField
    tarifa = models.IntegerField
    duracion = models.IntegerField
    lugar = models.CharField(max_length=200, default="Biblioteca")
    estado = models.CharField(max_length=200, default="Solicitada")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="usuario_tutorias")
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tutor_tutorias")

    def __str__(self):
        """Devuelve el nombre de la tutoria junto a su tema"""
        return "Tutoria: " + self.nombre + ". (" + self.tema + ")"
    
    def addCalendario(self):
        """Agrega la tutoria al calendario"""
        
        start_time = datetime.datetime.strptime(self.fecha,"%Y-%m-%d %H:%M:%S")
        end_time= start_time + timedelta(minutes=120)

        scopes = ['https://www.googleapis.com/auth/calendar']
        credentials = pickle.load(open('H:\\django projects\\token.pkl', 'rb'))
        service = build('calendar', 'v3', credentials=credentials)

        event = (
            service.events()
            .insert(
                calendarId="primary",
                body={
                    "summary": self.nombre,
                
                    "start": {"dateTime": start_time.isoformat(),
                    'timeZone': 'America/Bogota',
                
                    
                    },
                    "end": {
                        "dateTime": end_time.isoformat(),
                        'timeZone': 'America/Bogota',
                    },
                    "attendees":[{"email":self.usuario.email}
                    
                    ]
                },
            ).execute()
        )