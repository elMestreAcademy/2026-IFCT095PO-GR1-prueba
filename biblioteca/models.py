from django.db import models


# ===========================================================
# EJERCICIO 1 — Modelos Autor y Libro (20 puntos)
# ===========================================================
# TODO: Define dos modelos:
#
# Autor:
#   - nombre: texto, máximo 150 caracteres
#   - email: email, único
#   - activo: booleano, por defecto True
#
# Libro:
#   - titulo: texto, máximo 300 caracteres
#   - autor: FK a Autor (SET_NULL si se borra, permite null)
#   - precio: decimal, 8 dígitos, 2 decimales
#   - publicado: fecha, puede estar vacía/nula
#   - autores_secundarios: M2M con Autor (puede estar vacía)
#
# Añade a Libro un método precio_con_iva() que devuelva
# precio * 1.21, redondeado a 2 decimales.
# ===========================================================
