from django.shortcuts import render
from .models import Producto


# PAGINA PRINCIPAL
def inicio(request):

    productos = Producto.objects.all()

    buscar = request.GET.get('buscar')

    if buscar:
        productos = Producto.objects.filter(nombre__icontains=buscar)

    return render(request, 'inicio.html', {
        'productos': productos
    })


# CATEGORIAS
def hombres(request):
    productos = Producto.objects.filter(categoria='Hombre')
    return render(request, 'hombres.html', {'productos': productos})


def mujeres(request):
    productos = Producto.objects.filter(categoria='Mujer')
    return render(request, 'mujeres.html', {'productos': productos})


def niñas(request):
    productos = Producto.objects.filter(categoria='Niña')
    return render(request, 'niñas.html', {'productos': productos})


def niños(request):
    productos = Producto.objects.filter(categoria='Niño')
    return render(request, 'niños.html', {'productos': productos})