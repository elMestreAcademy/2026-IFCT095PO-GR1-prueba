from django.shortcuts import render, get_object_or_404, redirect


# ===========================================================
# EJERCICIO 2 — Vista libros_por_autor (10 puntos)
# ===========================================================
# TODO: Importa los modelos necesarios y completa la vista:
#   - Recibe request y autor_id
#   - Obtiene el Autor o 404
#   - Filtra libros de ese autor con publicado no nulo
#   - Renderiza 'biblioteca/por_autor.html' con autor y libros
# ===========================================================

def libros_por_autor(request, autor_id):
    pass  # ← TU CÓDIGO AQUÍ


# ===========================================================
# EJERCICIO 3c — Vista crear_libro (7 puntos)
# ===========================================================
# TODO: Completa la vista:
#   - GET: muestra formulario vacío
#   - POST: valida, si ok guarda y redirige a libros-por-autor
#     del autor correspondiente; si no, muestra errores
#   - Template: 'biblioteca/crear.html'
# ===========================================================

def crear_libro(request):
    pass  # ← TU CÓDIGO AQUÍ
