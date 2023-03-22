from django.urls import path
from . import views

urlpatterns = [
    path('tutorias/<str:email>', views.tutorias, name='tutorias'),
    path('detalle_tutoria/<str:tutoria_id>', views.detalle_tutoria, name='detalleTutoria'),
    path('solicitarTutoria/<str:emailtutor>/<str:emailestudiante>', views.solicitarTutoria, name='solicitarTutoria'),
    path('eliminar_tutoria/', views.eliminar_tutoria),
]
