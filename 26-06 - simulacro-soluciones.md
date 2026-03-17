# SIMULACRO — IFCT095PO Python y Django

**Duración:** 60 minutos | **Puntuación total:** 10 puntos
*mínimo*

- *1,5/4 en test*
- *1,5/6 en práctico*

## Instrucciones:

1. Clonad el repositorio:

```bash
git clone https://github.com/elMestreAcademy/2026-IFCT095PO-GR1-prueba
```

2. Responded sobre el fichero RESPUESTA.md

---

## PARTE A — TEST (4 puntos)

**Instrucciones:** Marque la respuesta correcta. Cada pregunta vale 0,5 puntos. No se penalizan errores.

**1.** ¿Cuál es la salida de `print(3 * "ab")`?

- a) `3ab`
- b) `ababab`
- c) `ab3`
- d) Error de tipo

**2.** ¿Qué comando crea una nueva aplicación llamada `blog` dentro de un proyecto Django existente?

- a) `django-admin startproject blog`
- b) `python manage.py startapp blog`
- c) `python manage.py newapp blog`
- d) `django-admin createapp blog`

**3.** ¿Cuál es el resultado de `len({"a": 1, "b": 2, "a": 3})`?

- a) `3`
- b) `2`
- c) `6`
- d) Error: clave duplicada

**4.** ¿Qué comando genera los ficheros de migración tras modificar un modelo?

- a) `python manage.py migrate`
- b) `python manage.py makemigrations`
- c) `python manage.py sqlmigrate`
- d) `python manage.py dbsync`

**5.** ¿Cómo se instancia un formulario Django con los datos recibidos de una petición POST?

- a) `MiForm(data=request.body)`
- b) `MiForm(request.POST)`
- c) `MiForm.from_post(request)`
- d) `MiForm(fields=request.POST)`

**6.** ¿Qué método devuelve el número total de registros de un QuerySet?

- a) `queryset.size()`
- b) `queryset.count()`
- c) `queryset.length()`
- d) `len(queryset)`


**7.** ¿Qué atributo de `ModelAdmin` define las columnas visibles en el listado?

- a) `fields`
- b) `list_display`
- c) `columns`
- d) `display_fields`

**8.** ¿Qué middleware Django gestiona la protección contra ataques CSRF?

- a) `django.middleware.security.SecurityMiddleware`
- b) `django.contrib.auth.middleware.CSRFMiddleware`
- c) `django.middleware.common.CsrfMiddleware`
- d) `django.middleware.csrf.CsrfViewMiddleware`

## PARTE B — EJERCICIOS PRÁCTICOS (6 puntos)

### Ejercicio 1 — Modelo con relación y método personalizado (2 puntos)

Defina dos modelos Django: `Autor` y `Libro`.

**Autor:**

- `nombre`: texto, máximo 150 caracteres
- `email`: email, único
- `activo`: booleano, por defecto `True`

**Libro:**

- `titulo`: texto, máximo 300 caracteres
- `autor`: clave foránea a `Autor` (si se borra el autor, el libro mantiene el campo como `NULL`)
- `precio`: decimal, 8 dígitos totales, 2 decimales
- `publicado`: fecha, puede estar vacía/nula
- `autores_secundarios`: relación muchos-a-muchos con `Autor` (puede estar vacía)

Añada al modelo `Libro` un método `precio_con_iva(self)` que devuelva el precio multiplicado por 1.21 redondeado a 2 decimales.

### Ejercicio 2 — Vista con filtro + URL (2 puntos)

Escriba:

**a)** Una vista basada en función llamada `libros_por_autor` que:

- Reciba `request` y un parámetro `autor_id`
- Obtenga el objeto `Autor` o devuelva un 404 si no existe
- Filtre los libros de ese autor que tengan fecha de publicación (`publicado` no nulo)
- Pase al template `libros/por_autor.html` el autor y los libros

**b)** La entrada en `urls.py` que mapee la ruta `autor/<int:autor_id>/libros/` a esa vista con el nombre `libros-por-autor`.

**c)** El template `libros/por_autor.html` que:

- Extienda de `base.html`
- Muestre como título `<h1>` el nombre del autor
- Liste los libros en una lista `<ul>` mostrando título y precio con IVA (usando el método del modelo)
- Si no hay libros, muestre "Este autor no tiene libros publicados."

---

### Ejercicio 3 — Formulario, validación cruzada y vista de procesamiento (2 puntos)

**a)** Cree un `ModelForm` llamado `LibroForm` para `Libro` con campos: `titulo`, `precio`, `publicado`, `autor`.

**b)** Implemente una validación en el método `clean()` del formulario que verifique: si el campo `publicado` tiene fecha, el `precio` no puede ser 0. Si se incumple, lance un `ValidationError` con el mensaje "Un libro publicado debe tener precio mayor que 0."

**c)** Escriba una vista `crear_libro` que:

- En GET: muestre el formulario vacío
- En POST: valide el formulario; si es válido lo guarde y redirija a `libros-por-autor` del autor correspondiente; si no es válido, vuelva a mostrar el formulario con los errores
- Use el template `libros/crear.html`

## CLAVE DE CORRECCIÓN

### Parte A — Respuestas test

| Preg. | Resp. |
| ----- | ----- |
| 1     | b     |
| 2     | b     |
| 3     | a     |
| 4     | b     |
| 5     | b     |
| 6     | c     |
| 7     | b     |
| 8     | d     |

### Parte B — Soluciones orientativas

**Ejercicio 1:**

```python
from django.db import models
from decimal import Decimal, ROUND_HALF_UP

class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.ForeignKey(
        Autor, on_delete=models.SET_NULL, null=True
    )
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
```

**Ejercicio 2a:**

```python
from django.shortcuts import render, get_object_or_404
from .models import Autor, Libro

def libros_por_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    libros = Libro.objects.filter(
        autor=autor, publicado__isnull=False
    )
    return render(request, 'libros/por_autor.html', {
        'autor': autor,
        'libros': libros,
    })
```

**Ejercicio 2b:**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('autor/<int:autor_id>/libros/',
         views.libros_por_autor,
         name='libros-por-autor'),
]
```

**Ejercicio 2c:**

```html
{% extends "base.html" %} {% block content %}
<h1>{{ autor.nombre }}</h1>
{% if libros %}
<ul>
  {% for libro in libros %}
  <li>{{ libro.titulo }} — {{ libro.precio_con_iva }} €</li>
  {% endfor %}
</ul>
{% else %}
<p>Este autor no tiene libros publicados.</p>
{% endif %} {% endblock %}
```

**Ejercicio 3a + 3b:**

```python
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'precio', 'publicado', 'autor']

    def clean(self):
        cleaned = super().clean()
        publicado = cleaned.get('publicado')
        precio = cleaned.get('precio')
        if publicado and precio is not None and precio == 0:
            raise forms.ValidationError(
                'Un libro publicado debe tener precio mayor que 0.'
            )
        return cleaned
```

**Ejercicio 3c:**

```python
from django.shortcuts import render, redirect
from .forms import LibroForm

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            return redirect('libros-por-autor',
                            autor_id=libro.autor_id)
    else:
        form = LibroForm()
    return render(request, 'libros/crear.html', {'form': form})
```

### Rúbrica Parte B (por ejercicio, 2 pts)

| Criterio                                       | Puntos |
| ---------------------------------------------- | ------ |
| Sintaxis correcta, código ejecutable           | 0,8    |
| Funcionalidad completa según enunciado         | 0,8    |
| Buenas prácticas (naming, estructura, imports) | 0,4    |
