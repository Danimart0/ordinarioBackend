from django.contrib import admin
from .models import Usuario, Categoria, Proveedor, Producto, HistorialMovimiento

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(HistorialMovimiento)
