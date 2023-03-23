from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_singup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    # Agregar otras rutas aquí
]