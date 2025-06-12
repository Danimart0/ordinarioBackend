from rest_framework import viewsets
from .models import Producto, Categoria, Proveedor, HistorialMovimiento, Usuario
from .serializers import ProductoSerializer, CategoriaSerializer, ProveedorSerializer, HistorialSerializer, UsuarioSerializer
from django.contrib.auth import get_user_model
from .serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
   

    def get_serializer_context(self):
        return {'request': self.request}

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class HistorialViewSet(viewsets.ReadOnlyModelViewSet):  
    queryset = HistorialMovimiento.objects.all()
    serializer_class = HistorialSerializer


Usuario = get_user_model()

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Usuario.objects.filter(id=self.request.user.id)
