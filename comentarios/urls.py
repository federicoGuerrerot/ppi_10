from django.urls import path
from . import views

urlpatterns = [
    path('comentarios/', views.listarcomentarios, name='comentarios'),
    path('calificar/<str:comentario_id>', views.calificar, name='calificar'),
]