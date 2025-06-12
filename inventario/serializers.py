from rest_framework import serializers
from .models import Producto, Categoria, Proveedor, HistorialMovimiento
from django.contrib.auth import get_user_model


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialMovimiento
        fields = '__all__'

Usuario = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
