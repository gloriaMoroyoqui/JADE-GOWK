from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# ==========================================
# 1. PRODUCTOS
# ==========================================
class Producto(models.Model):
    CATEGORIAS = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        ('Niña', 'Niña'),
        ('Niño', 'Niño'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    talla = models.CharField(max_length=10)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre


# ==========================================
# 2. PERFIL DE USUARIO (EXTENDIDO)
# ==========================================
class Perfil(models.Model):
    # Relaciona el perfil directamente con el usuario de Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    foto = models.ImageField(upload_to='perfiles/', default='perfiles/default.png', blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

# SEÑALES AUTOMÁTICAS: Crean el perfil en la base de datos justo al registrar un usuario
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.perfil.save()


# ==========================================
# 3. CARRITO DE COMPRAS
# ==========================================
class Carrito(models.Model):
    # Ahora cada carrito le pertenece obligatoriamente a un usuario registrado
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carritos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username} - ID {self.id}"


# ==========================================
# 4. ITEMS DEL CARRITO
# ==========================================
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"
    
    # Función útil para calcular el subtotal de este producto en el carrito
    def obtener_subtotal(self):
        return self.cantidad * self.producto.precio


# ==========================================
# 5. LISTA DE DESEOS (FAVORITOS)
# ==========================================
class ListaDeseos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lista_deseos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Esto evita que un usuario agregue el mismo producto dos veces a favoritos
        unique_together = ('usuario', 'producto')

    def __str__(self):
        return f"{self.usuario.username} quiere {self.producto.nombre}"


# ==========================================
# 6. COMENTARIOS Y RESEÑAS
# ==========================================
class Comentario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.producto.nombre}"