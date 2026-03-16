# Respuestas

### Alumno/a: Carlos Mestre
### DNI: 12345678Z

## Tipo Test

| Pregunta  | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ---       | --- | --- | --- | --- | --- | --- | --- | --- |
| Respuesta | b   | b   | a   | b   |     |     |     |     |

## Supuesto práctico

**Ejercicio 1:**

```python

# biblioteca/models.py

class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    activeo = models.BooleanField(default=True)

class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.(Autor, on_delete=models.SET_NULL)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    publicado = models.DateTimeField()
    # Autores secundarios, de momento en blanco que es la chunga (xa 10)

    def precio_con_iva(self):
        return float(self.precio) * 1.21
```

**Ejercicio 2a:**

```python
# biblioteca/views.py
def libros_por_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    libros = Libro.objects.filter(autor_id = autor_id)
    # libros = Libro.objects.filter(autor_id = autor_id, publicado_isnull = False)

    return render(
        request,
        "biblioteca/por_autor.html",
        {
            "autor": autor,
            "libros": libros,
        },
    )
```

**Ejercicio 2b:**

```python
# urls.py
path(" autor/<int:autor_id>/libros/", views.libros_por_autor, name="Libros por autor")
```

**Ejercicio 2c:**

```html
<!-- por_autor_html -->
{% block content %}

  {% if libros %}

    {% for libro in libros %}
      libro.titulo
      libro.precio_con_iva()
    {% endfor %}

  {% else %}
    Este autor no tiene libros publicados.
  {% endif %}

{% endblock %}
```

**Ejercicio 3a:**

```python
## Código aquí
```

**Ejercicio 3b:**

```python
## Código aquí
```

**Ejercicio 3c:**

```python
## Código aquí
```
