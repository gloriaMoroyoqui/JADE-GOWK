from django.contrib import admin
from .models import Producto, Carrito, ItemCarrito, Comentario, ListaDeseos, Perfil

admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(Comentario)
admin.site.register(ListaDeseos)
admin.site.register(Perfil)