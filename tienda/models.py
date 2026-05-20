from django.db import models


# PRODUCTOS
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


# CARRITO
class Carrito(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito {self.id}"


# ITEMS DEL CARRITO
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"


# COMENTARIOS
class Comentario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario


# LISTA DE DESEOS
class ListaDeseos(models.Model):
    usuario = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario


# PERFIL
class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return self.nombre