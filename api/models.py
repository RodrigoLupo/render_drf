from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Proveedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos_acumulados = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    dni = models.CharField(max_length=8, unique=True)
    ruc = models.CharField(max_length=11, blank=True, null=True)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

class Producto(models.Model):
    TIPO_PRODUCTO_CHOICES = [
        ('V', 'Venta'),
        ('C', 'Canje'),
    ]
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    puntos_requeridos = models.PositiveIntegerField(null=True, blank=True)
    tipo = models.CharField(max_length=1, choices=TIPO_PRODUCTO_CHOICES)

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    TIPO_TRANSACCION_CHOICES = [
        ('V', 'Venta'),
        ('C', 'Canje'),
    ]
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    puntos_utilizados = models.PositiveIntegerField(null=True, blank=True)
    tipo = models.CharField(max_length=1, choices=TIPO_TRANSACCION_CHOICES)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo} - {self.producto.nombre} - {self.fecha}'

class KiloProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    kilos = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=2000, default="")

    def __str__(self):
        return f'{self.proveedor.user.username} - {self.kilos} kg - {self.fecha}'

class Configuracion(models.Model):
    conversion_rate = models.PositiveIntegerField(default=100)

class SensorData(models.Model):
    temperature = models.FloatField(default=0.0)
    humidity = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)

class ServoMotorState(models.Model):
    is_active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)