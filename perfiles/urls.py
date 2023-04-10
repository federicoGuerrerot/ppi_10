from django.urls import path
from . import views

urlpatterns = [
    path('mi_perfil/', views.mi_perfil, name='mi_perfil'),
]
