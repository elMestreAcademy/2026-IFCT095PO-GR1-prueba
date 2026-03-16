import decimal

from django.db import models

# ===========================================================
# EJERCICIO 1 - Modelos Autor y Libro (20 puntos)
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

class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    activo = models.BooleanField(default=True)

class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    publicado = models.DateTimeField()
    # Autores secundarios, de momento en blanco que es la chunga (xa 10)

    def precio_con_iva(self):
        return float(self.precio) * 1.21
        # return round(float(self.precio) * 1.21 ,2)
        # return self.precio * decimal.Decimal('1.21')
