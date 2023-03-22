from django.urls import path
from . import views

urlpatterns = [
    path('tutorias/<str:id>', views.tutorias, name='tutorias'),
    path('detalle_tutoria/<int:tutoria_id>', views.detalle_tutoria, name='detalleTutoria'),
    path('crear_tutoria/', views.crear_tutoria),
    path('eliminar_tutoria/', views.eliminar_tutoria),
]
