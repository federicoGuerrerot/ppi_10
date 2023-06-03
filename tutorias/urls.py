from django.urls import path
from . import views

urlpatterns = [
    path('tutorias/', views.tutorias, name='tutorias'),
    path('agendar/<str:tutoria_id>', views.agendar, name='agendar'),
    path('solicitar_tutoria/<str:emailtutor>', views.solicitarTutoria, name='solicitarTutoria'),
    path('aceptar_tutoria/<str:tutoria_id>', views.aceptar_tutoria, name='aceptarTutoria'),
    path('rechazar_tutoria/<str:tutoria_id>', views.rechazar_tutoria, name='rechazarTutoria'),
    path('eliminar_tutoria/<str:tutoria_id>', views.eliminar_tutoria, name='eliminarTutoria'),
    path('test_api/<str:tutoria_id>', views.test_api, name='test_api'),
    path('test_api2/', views.test_api2, name='test_api2'),
]
