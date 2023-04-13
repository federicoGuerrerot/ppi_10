from django.urls import path
from . import views

urlpatterns = [
    path('tutorias/', views.tutorias, name='tutorias'),
    path('detalle_tutoria/<str:tutoria_id>', views.detalle_tutoria, name='detalleTutoria'),
    path('solicitar_tutoria/<str:emailtutor>', views.solicitarTutoria, name='solicitarTutoria'),
    path('aceptar_tutoria/<str:tutoria_id>', views.aceptar_tutoria, name='aceptarTutoria'),
    path('rechazar_tutoria/<str:tutoria_id>', views.rechazar_tutoria, name='rechazarTutoria'),
    path('eliminar_tutoria/<str:tutoria_id>', views.eliminar_tutoria, name='eliminarTutoria'),
    
]
