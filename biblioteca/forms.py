from django import forms


# ===========================================================
# EJERCICIO 3a+3b - LibroForm con validación cruzada (13 puntos)
# ===========================================================
# TODO:
#   a) Crea un ModelForm para Libro con campos:
#      titulo, precio, publicado, autor
#   b) En clean(): si publicado tiene fecha y precio == 0,
#      lanza ValidationError:
#      "Un libro publicado debe tener precio mayor que 0."
# ===========================================================
