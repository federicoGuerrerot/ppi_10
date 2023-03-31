from django.urls import path
from . import views

urlpatterns = [
    path('tutorias/', views.tutorias, name='tutorias'),
    path('detalle_tutoria/<str:tutoria_id>', views.detalle_tutoria, name='detalleTutoria'),
    path('solicitar_tutoria/<str:emailtutor>', views.solicitarTutoria, name='solicitarTutoria'),
    path('eliminar_tutoria/<str:tutoria_id>', views.eliminar_tutoria, name='eliminarTutoria'),
    
]
