from django.urls import path
from . import views

urlpatterns = [
    path('tutorias/<str:tutor>', views.tutorias, name='tutorias'),
    path('detalle_tutoria/<int:tutoria_id>', views.detalle_tutoria, name='detalleTutoria'),
    path('solicitarTutoria/<str:emailtutor>', views.solicitarTutoria, name='solicitarTutoria'),
    path('eliminar_tutoria/', views.eliminar_tutoria),
]
