from django.urls import path
from . import views

urlpatterns = [
    path('inbox', views.Inbox, name='inbox'),
    path('buscarUsuario', views.buscarUsuario, name='buscarUsuario'),
    path('enviar', views.enviar, name='enviar'),
    path('nuevaConversacion/<str:email>', views.nuevaConversacion, name='nuevaConversacion'),
    path('directs/<str:email>', views.directs, name='directs'),
]
