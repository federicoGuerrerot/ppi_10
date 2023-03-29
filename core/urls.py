from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tutor/<slug:tutorslug>', views.tutor, name='tutor'),
    path('buscar/<slug:slug>', views.buscar, name='buscar'),
]
