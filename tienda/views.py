from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Producto, Carrito, ItemCarrito, ListaDeseos, Perfil
from .forms import RegistroForm, UserUpdateForm, PerfilUpdateForm

# ==========================================
# 1. CATÁLOGOS Y NAVEGACIÓN PÚBLICA
# ==========================================

# PAGINA PRINCIPAL
def inicio(request):
    productos = Producto.objects.all()
    buscar = request.GET.get('buscar')

    if buscar:
        productos = Producto.objects.filter(nombre__icontains=buscar)

    return render(request, 'tienda/inicio.html', {
        'productos': productos
    })


# CATEGORIAS DE ROPA
def hombres(request):
    productos = Producto.objects.filter(categoria='Hombre')
    return render(request, 'tienda/hombres.html', {'productos': productos})


def mujeres(request):
    productos = Producto.objects.filter(categoria='Mujer')
    return render(request, 'tienda/mujeres.html', {'productos': productos})


def niñas(request):
    productos = Producto.objects.filter(categoria='Niña')
    return render(request, 'tienda/niñas.html', {'productos': productos})


def niños(request):
    productos = Producto.objects.filter(categoria='Niño')
    return render(request, 'tienda/niños.html', {'productos': productos})


# ==========================================
# 2. AUTENTICACIÓN Y PERFIL DE USUARIO
# ==========================================

# REGISTRO DE USUARIOS
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente tras registrarse
            messages.success(request, f"¡Bienvenido a JADE & GOWK, {user.first_name}!")
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'tienda/registrar.html', {'form': form})


# VER Y EDITAR PERFIL (SÓLO USUARIOS LOGUEADOS)
@login_required
def ver_perfil(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PerfilUpdateForm(request.POST, request.FILES, instance=request.user.perfil)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "¡Tu perfil ha sido actualizado con éxito!")
            return redirect('perfil')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PerfilUpdateForm(instance=request.user.perfil)

    return render(request, 'tienda/perfil.html', {
        'u_form': u_form,
        'p_form': p_form
    })


# ==========================================
# 3. SISTEMA DE CARRITO DE COMPRAS
# ==========================================

# VER EL CARRITO
@login_required
def ver_carrito(request):
    # Obtiene o crea el carrito único del usuario
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()
    
    # Suma el subtotal de cada ítem para dar el total final
    total = sum(item.obtener_subtotal() for item in items)
    
    return render(request, 'tienda/cart_detail.html', {
        'carrito': carrito,
        'items': items,
        'total': total
    })


# AGREGAR AL CARRITO
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    
    # Si la prenda ya está en el carrito, le sumamos 1 a la cantidad, si no, se crea el registro
    item_carrito, item_created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not item_created:
        item_carrito.cantidad += 1
        item_carrito.save()
        messages.info(request, f"Se añadió otra unidad de {producto.nombre} a tu carrito.")
    else:
        messages.success(request, f"¡{producto.nombre} añadido al carrito con éxito!")
        
    return redirect('ver_carrito')


# ELIMINAR DEL CARRITO
@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    item.delete()
    messages.warning(request, "Producto removido del carrito.")
    return redirect('ver_carrito')


# ==========================================
# 4. SISTEMA DE LISTA DE DESEOS (FAVORITOS)
# ==========================================

# VER LISTA DE DESEOS
@login_required
def ver_lista_deseos(request):
    deseos = ListaDeseos.objects.filter(usuario=request.user)
    return render(request, 'tienda/lista_deseos.html', {'deseos': deseos})


# AGREGAR A LISTA DE DESEOS
@login_required
def agregar_a_deseos(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    deseo, created = ListaDeseos.objects.get_or_create(usuario=request.user, producto=producto)
    
    if created:
        messages.success(request, f"¡{producto.nombre} se guardó en tu lista de deseos! ❤️")
    else:
        messages.info(request, f"{producto.nombre} ya está en tus favoritos.")
        
    return redirect('ver_lista_deseos')


# ELIMINAR DE LISTA DE DESEOS
@login_required
def eliminar_de_deseos(request, deseo_id):
    deseo = get_object_or_404(ListaDeseos, id=deseo_id, usuario=request.user)
    deseo.delete()
    messages.warning(request, "Prenda eliminada de tus favoritos.")
    return redirect('ver_lista_deseos')