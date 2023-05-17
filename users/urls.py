from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),

]