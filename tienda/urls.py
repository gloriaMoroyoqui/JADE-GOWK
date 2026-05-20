from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),

    path('hombres/', views.hombres, name='hombres'),
    path('mujeres/', views.mujeres, name='mujeres'),
    path('niñas/', views.niñas, name='niñas'),
    path('niños/', views.niños, name='niños'),

]