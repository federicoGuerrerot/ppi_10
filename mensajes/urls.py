from django.urls import path
from . import views

urlpatterns = [
    path('enviar', views.enviar, name='enviar'),
    path('nuevaConversacion/<str:email>/<str:tutoria_id>', views.nuevaConversacion, name='nuevaConversacion'),
    path('directs/<str:email>/<str:tutoria_id>', views.directs, name='directs'),
]
