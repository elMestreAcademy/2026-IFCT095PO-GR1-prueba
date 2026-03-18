from django.urls import path

from . import views

app_name = 'biblioteca'

urlpatterns = [
    path('', views.lista_libros, name='lista-libros'),
    path('autor/<int:autor_id>/libros/', views.libros_por_autor, name='libros-por-autor'),
    path('libro/<int:libro_id>/', views.detalle_libro, name='detalle-libro'),
    path('libro/nuevo/', views.crear_libro, name='crear-libro'),
]
