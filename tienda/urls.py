from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ==========================================
    # 1. CATÁLOGOS Y NAVEGACIÓN PÚBLICA
    # ==========================================
    path('', views.inicio, name='inicio'),
    path('hombres/', views.hombres, name='hombres'),
    path('mujeres/', views.mujeres, name='mujeres'),
    path('niñas/', views.niñas, name='niñas'),
    path('niños/', views.niños, name='niños'),

    # ==========================================
    # 2. AUTENTICACIÓN Y PERFIL DE USUARIO
    # ==========================================
    path('registrar/', views.registrar_usuario, name='registrar'),
    # Django busca por defecto la plantilla 'registration/login.html', aquí la redirigimos a tu carpeta 'tienda'
    path('login/', auth_views.LoginView.as_view(template_name='tienda/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    
    # Perfil del usuario
    path('perfil/', views.ver_perfil, name='perfil'),
    # Vista nativa para cambiar contraseña de forma segura. Al tener éxito, te regresa al perfil.
    path('perfil/cambiar-password/', auth_views.PasswordChangeView.as_view(
        template_name='tienda/cambiar_password.html',
        success_url='/perfil/'
    ), name='cambiar_password'),

    # ==========================================
    # 3. SISTEMA DE CARRITO DE COMPRAS
    # ==========================================
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),

    # ==========================================
    # 4. SISTEMA DE LISTA DE DESEOS (FAVORITOS)
    # ==========================================
    path('deseos/', views.ver_lista_deseos, name='ver_lista_deseos'),
    path('deseos/agregar/<int:producto_id>/', views.agregar_a_deseos, name='agregar_a_deseos'),
    path('deseos/eliminar/<int:deseo_id>/', views.eliminar_de_deseos, name='eliminar_de_deseos'),
]