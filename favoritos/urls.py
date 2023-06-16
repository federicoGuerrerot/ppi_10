from django.urls import path
from . import views

urlpatterns = [
    path('favoritos/', views.favoritos, name='favoritos'),
    path('añadirFavorito/<str:emailtutor>', views.añadirFavorito, name='añadirFavorito'),
    path('eliminarFavorito/<str:emailtutor>', views.eliminarFavorito, name='eliminarFavorito'),
]
