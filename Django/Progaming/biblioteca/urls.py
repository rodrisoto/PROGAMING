from django.contrib.auth import views as auth_views
from django.urls import path
from .views import libros, crear, recuperar_contraseña, categoria2, categoria3, categoria4, categoria5
from .views import CustomLogoutView
from . import views

urlpatterns = [
    path('libros/', libros, name="libros"),
    path('crear/', crear, name="crear"),
    
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html',  next_page='/libros/'), name="login"),
    path('accounts/logout/', CustomLogoutView.as_view(next_page='/login/'), name='logout'),
    
    path('recuperar_contraseña/', recuperar_contraseña, name="recuperar_contraseña"),
    path('categoria2/', categoria2, name="categoria2"),
    path('categoria3/', categoria3, name="categoria3"),
    path('categoria4/', categoria4, name="categoria4"),
    path('categoria5/', categoria5, name="categoria5"),


    path('juegos/', views.listar_juegos, name='listar_juegos'),
    path('juegos/agregar/', views.agregar_juego, name='agregar_juego'),
    path('juegos/modificar/<int:juego_id>/', views.editar_juego, name='editar_juego'),
    path('juegos/eliminar/<int:juego_id>/', views.eliminar_juego, name='eliminar_juego'),
]
