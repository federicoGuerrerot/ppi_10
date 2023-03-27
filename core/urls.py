from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tutor/<slug:tutor_slug>', views.tutor, name='tutor'),
]
