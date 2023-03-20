from django.urls import path
from . import views

urlpatterns = [
    path('tutorias/', views.tutorias),
    path('ver_tutoria/', views.ver_tutoria, name='vistaTutoria'),
    path('crear_tutoria/', views.crear_tutoria),
    path('eliminar_tutoria/', views.eliminar_tutoria),
]
