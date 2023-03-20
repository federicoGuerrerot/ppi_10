from django.urls import path
from . import views

urlpatterns = [
    path('tutoria/', views.vistaTutoria, name='vistaTutoria'),
]
