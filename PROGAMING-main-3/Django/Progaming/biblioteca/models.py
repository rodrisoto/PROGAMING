from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    is_admin = models.BooleanField(default=False)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    plataforma = models.CharField(
        max_length=20,
        choices=[
            ('pc', 'PC'),
            ('playstation', 'PlayStation'),
            ('xbox', 'Xbox'),
            ('nintendo', 'Nintendo'),
            ('movil', 'Móvil'),
        ],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Juegos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='juegos')
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.username}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juegos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle del pedido {self.pedido.id} - Juego {self.juego.nombre}"

class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juegos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'juego'], name='unique_carrito')
        ]

    
    def __str__(self):
        return f"Carrito de {self.usuario.username} - Juego {self.juego.nombre}"