from rest_framework import serializers
from .models import Proveedor, Cliente, Producto, Transaccion, KiloProveedor, Configuracion,SensorData,ServoMotorState
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['id', 'user', 'puntos_acumulados']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellidos', 'dni', 'ruc', 'ubicacion']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'puntos_requeridos', 'tipo']

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = ['id', 'proveedor', 'cliente', 'producto', 'cantidad', 'total', 'puntos_utilizados', 'tipo', 'fecha']

class KiloProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = KiloProveedor
        fields = ['id', 'proveedor', 'kilos', 'descripcion', 'fecha']
        
class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = ['conversion_rate']
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['temperature','humidity']
class ServoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServoMotorState
        fields = ['is_active']