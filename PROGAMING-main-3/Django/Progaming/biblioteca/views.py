from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroUsuarioForm, JuegosForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .models import Juegos, Pedido, DetallePedido
from django.http import JsonResponse
import requests
from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JuegosSerializer, PedidoSerializer, DetallePedidoSerializer


class JuegosViewset(viewsets.ModelViewSet):
    queryset = Juegos.objects.all()
    serializer_class = JuegosSerializer


class PedidoViewset(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetallePedidoViewset(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


def external_page(request):
  
    return render(request, "juegos/external.html")

def api_rawg(request):
    url = "https://api.rawg.io/api/games"
    params = {
        "key": settings.RAWG_API_KEY,
        "ordering": "-rating",
        "page_size": 10
    }
    resp = requests.get(url, params=params, timeout=5)
    resultados = resp.json().get("results", [])
    juegos = [
        {"nombre": j["name"], "imagen": j["background_image"], "rating": j["rating"], "slug": j["slug"]}
        for j in resultados
    ]
    return JsonResponse({"juegos": juegos})

def api_freetogame(request):
    resp = requests.get("https://www.freetogame.com/api/games", timeout=5)
    data = resp.json()[:10]
    juegos = [
        {
          "nombre": j["title"],
          "imagen": j["thumbnail"],
          "plataforma": j["platform"],
          "genero": j["genre"],
          "url": j["game_url"]
        }
        for j in data
    ]
    return JsonResponse({"juegos": juegos})

# Create your views here.
def libros(request):
    print("accediendo a la vista libros")
    return render(request, 'index.html')


def crear(request):
    print("Accediendo a la vista crear")

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)  # Recibimos los datos del formulario
        if form.is_valid():  # Si los datos son válidos
            form.save()  # Guardamos el usuario en la base de datos
            return redirect('login')  # Redirigimos a la página de inicio de sesión
        else:
            print(form.errors)  # Imprime los errores de validación en la consola para depuración
    else:
        form = RegistroUsuarioForm()  # Si es GET, mostramos un formulario vacío

    return render(request, 'registro.html', {'form': form})


def login(request):
    return render(request, 'login.html')

def recuperar_contraseña(request):
    return render(request, 'recuperar_contraseña.html')

def categoria2(request):
    return render(request, 'categoria2.html')

def categoria3(request):
    return render(request, 'categoria3.html')

def categoria4(request):
    return render(request, 'categoria4.html')

def categoria5(request):
    return render(request, 'categoria5.html')

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "¡Has cerrado sesión correctamente!")
        return super().dispatch(request, *args, **kwargs)
    



def listar_juegos(request):
    juegos = Juegos.objects.all()
    return render(request, 'juegos/listar.html', {'juegos': juegos})


def agregar_juego(request):
    if request.method == 'POST':
        form = JuegosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego agregado correctamente.')
            return redirect('listar_juegos')
    else:
        form = JuegosForm()
    return render(request, 'juegos/agregar.html', {'form': form})


def editar_juego(request, juego_id):
    juego = get_object_or_404(Juegos, pk=juego_id)
    if request.method == 'POST':
        form = JuegosForm(request.POST, request.FILES, instance=juego)
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego actualizado correctamente.')
            return redirect('listar_juegos')
    else:
        form = JuegosForm(instance=juego)
    return render(request, 'juegos/modificar.html', {'form': form, 'juego': juego})


def eliminar_juego(request, juego_id):
    juego = get_object_or_404(Juegos, pk=juego_id)
    if request.method == 'POST':
        juego.delete()
        messages.success(request, 'Juego eliminado correctamente.')
        return redirect('listar_juegos')
    return render(request, 'juegos/eliminar.html', {'juego': juego})

