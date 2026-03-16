from django.urls import path

from . import views

app_name = 'biblioteca'

# ===========================================================
# EJERCICIO 2b - URL (3 puntos)
# ===========================================================
# TODO: Añade la ruta que mapee:
#   autor/<int:autor_id>/libros/ → libros_por_autor
#   con name='libros-por-autor'
# Y la ruta:
#   libro/nuevo/ → crear_libro
#   con name='crear-libro'
# ===========================================================

urlpatterns = [
    # TU CÓDIGO AQUÍ
    path(" autor/<int:autor_id>/libros/", views.libros_por_autor, name="Libros por autor")
]
