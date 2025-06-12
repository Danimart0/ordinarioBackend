from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='perfiles/', null=True, blank=True)

    def __str__(self):
        return self.username

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='categorias/', blank=True, null=True)  

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, related_name='productos')
    stock = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  

    def __str__(self):
        return self.nombre


class HistorialMovimiento(models.Model):
    ACCIONES = (
        ('crear', 'Crear'),
        ('editar', 'Editar'),
        ('eliminar', 'Eliminar'),
    )

    accion = models.CharField(max_length=10, choices=ACCIONES)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    datos_anteriores = models.JSONField(null=True, blank=True)
    datos_nuevos = models.JSONField(null=True, blank=True)

    def __str__(self):
        entidad = self.producto or self.proveedor or self.categoria
        return f"{self.get_accion_display()} - {entidad} por {self.usuario} el {self.fecha_hora}"
