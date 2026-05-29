from django.contrib import admin
from .models import Producto, Perfil, Carrito, ItemCarrito, ListaDeseos, Comentario

# ==========================================
# 1. PANEL DE PRODUCTOS
# ==========================================
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que verás en la tabla principal
    list_display = ('nombre', 'precio', 'categoria', 'talla', 'stock')
    # Filtros rápidos en la barra lateral derecha
    list_filter = ('categoria', 'talla')
    # Buscador por nombre y descripción
    search_fields = ('nombre', 'descripcion')
    # Te permite editar el precio y el stock directamente desde la lista sin entrar al producto
    list_editable = ('precio', 'stock')


# ==========================================
# 2. PANEL DE PERFILES DE USUARIO
# ==========================================
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    # Muestra el nombre de usuario de Django, su correo, teléfono y dirección
    list_display = ('obtener_usuario', 'obtener_correo', 'telefono', 'direccion')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__email', 'telefono')

    # Funciones para traer datos limpios desde el modelo User integrado de Django
    def obtener_usuario(self, obj):
        return obj.usuario.username
    obtener_usuario.short_description = 'Usuario'

    def obtener_correo(self, obj):
        return obj.usuario.email
    obtener_correo.short_description = 'Correo Electrónico'


# ==========================================
# 3. PANEL DEL CARRITO (CON SUS ITEMS INTEGRADOS)
# ==========================================
# Esto permite ver y editar los ítems de un carrito dentro del mismo panel del Carrito principal
class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 0 # No añade filas vacías por defecto

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('obtener_usuario', 'fecha_creacion')
    search_fields = ('usuario__username',)
    inlines = [ItemCarritoInline] # Agrega los productos dentro del carrito en la misma vista

    def obtener_usuario(self, obj):
        return obj.usuario.username
    obtener_usuario.short_description = 'Dueño del Carrito'


# ==========================================
# 4. PANEL DE LISTA DE DESEOS
# ==========================================
@admin.register(ListaDeseos)
class ListaDeseosAdmin(admin.ModelAdmin):
    list_display = ('obtener_usuario', 'obtener_producto', 'fecha_agregado')
    search_fields = ('usuario__username', 'producto__nombre')

    def obtener_usuario(self, obj):
        return obj.usuario.username
    obtener_usuario.short_description = 'Usuario'

    def obtener_producto(self, obj):
        return obj.producto.nombre
    obtener_producto.short_description = 'Producto Favorito'


# ==========================================
# 5. PANEL DE COMENTARIOS
# ==========================================
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('obtener_usuario', 'obtener_producto', 'fecha', 'comentario_corto')
    list_filter = ('fecha',)
    search_fields = ('usuario__username', 'producto__nombre', 'comentario')

    def obtener_usuario(self, obj):
        return obj.usuario.username
    obtener_usuario.short_description = 'Usuario'

    def obtener_producto(self, obj):
        return obj.producto.nombre
    obtener_producto.short_description = 'Producto'

    # Recorta los comentarios largos en la vista de tabla para que no ocupe tanto espacio
    def comentario_corto(self, obj):
        return obj.comentario if len(obj.comentario) < 50 else f"{obj.comentario[:50]}..."
    comentario_corto.short_description = 'Comentario'