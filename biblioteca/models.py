from decimal import ROUND_HALF_UP, Decimal

from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    publicado = models.DateField(null=True, blank=True)
    autores_secundarios = models.ManyToManyField(
        Autor, related_name='libros_secundarios', blank=True
    )

    def precio_con_iva(self):
        return (self.precio * Decimal('1.21')).quantize(
            Decimal('0.01'), rounding=ROUND_HALF_UP
        )

    def __str__(self):
        return self.titulo
