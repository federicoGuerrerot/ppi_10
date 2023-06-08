from django.db import models
from django.conf import settings
import uuid #para crear id unicos, y que sirvan a la hora de migrar la base de datos, si lo vemos necesario.

# Librerias para el calendario
from datetime import timedelta
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

    def addCalendario(self,creds):
        """Agrega la tutoria al calendario"""

        # recuperar la fecha y hora de la tutoria
        start_time = self.fecha
        # Calcular la hora de finalizacion de la tutoria
        end_time= start_time + timedelta(minutes=120)
        
        try:
            # Crear servicio de google calendar
            service = build('calendar', 'v3', credentials=creds)

            # Crear evento en el calendario
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