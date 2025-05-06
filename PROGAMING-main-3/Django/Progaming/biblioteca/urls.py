from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.shortcuts import redirect
from .views import (
    libros, crear, recuperar_contraseña,
    categoria2, categoria3, categoria4, categoria5,
    CustomLogoutView, api_rawg, api_freetogame,
    external_page, JuegosViewset, PedidoViewset
)
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('juegos', JuegosViewset)
router.register('pedido', PedidoViewset)


urlpatterns = [
    path('libros/', libros, name="libros"),
    path('crear/', crear, name="crear"),

    
    # Login / logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html',  next_page='/libros/'), name="login"),
    path('accounts/logout/', CustomLogoutView.as_view(next_page='/login/'), name='logout'),
    

    # Otras vistas
    path('recuperar_contraseña/', recuperar_contraseña, name="recuperar_contraseña"),
    path('categoria2/', categoria2, name="categoria2"),
    path('categoria3/', categoria3, name="categoria3"),
    path('categoria4/', categoria4, name="categoria4"),
    path('categoria5/', categoria5, name="categoria5"),

    # CRUD de juegos
    path('juegos/', views.listar_juegos, name='listar_juegos'),
    path('juegos/agregar/', views.agregar_juego, name='agregar_juego'),
    path('juegos/modificar/<int:juego_id>/', views.editar_juego, name='editar_juego'),
    path('juegos/eliminar/<int:juego_id>/', views.eliminar_juego, name='eliminar_juego'),
    

    # Página que consume las APIs externas sin recarga
    path('juegos/external/', external_page, name='external_page'),

    # Endpoints JSON de las APIs externas
    path('api/rawg/', api_rawg, name='api_rawg'),
    path('api/free/', api_freetogame, name='api_freetogame'),

    path('api/', include(router.urls)),
    # raíz redirige a /libros/ (o a external_page si lo prefieres)
    path('', lambda request: redirect('libros', permanent=False)),

]










    

