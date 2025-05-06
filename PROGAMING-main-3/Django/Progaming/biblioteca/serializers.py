from .models import Juegos, Pedido, DetallePedido
from rest_framework import serializers



class JuegosSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(read_only=True, source='categoria.nombre')


    def validate_nombre(self, value):
        existe = Juegos.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Este juego ya existe")
        
        return value


    class Meta:
        model = Juegos
        fields = '__all__'



class DetallePedidoSerializer(serializers.ModelSerializer):
    juego = JuegosSerializer(read_only=True)

    class Meta:
        model = DetallePedido
        fields = ['juego', 'cantidad', 'subtotal']     

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'fecha', 'total', 'detalles']


