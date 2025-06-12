from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CategoriaViewSet, ProveedorViewSet, HistorialViewSet,  UsuarioViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'historial', HistorialViewSet)
router.register(r'usuarios', UsuarioViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
