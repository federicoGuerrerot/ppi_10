from django.urls import path
from . import views

urlpatterns = [
    path('favoritos/', views.favoritos, name='favoritos'),
]
