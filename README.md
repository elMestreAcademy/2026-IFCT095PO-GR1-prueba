# Examen práctico — IFCT095PO · Python y Django

## Instrucciones para el alumno

### 1. Preparar el entorno

```bash
# Activar el entorno virtual (si no existe, créalo primero)
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Aplicar migraciones y cargar datos de prueba

```bash
python manage.py migrate
```

### 3. Completar los TODO

Edita **únicamente** los siguientes archivos (busca las marcas `TODO`):

| Archivo                                          | Ejercicio                                 | Puntos |
| ------------------------------------------------ | ----------------------------------------- | ------ |
| `biblioteca/models.py`                           | Modelos `Autor` y `Libro`                 | 20     |
| `biblioteca/views.py`                            | Vistas `libros_por_autor` y `crear_libro` | 17     |
| `biblioteca/forms.py`                            | `LibroForm` con validación cruzada        | 13     |
| `biblioteca/urls.py`                             | Rutas de la app biblioteca                | 3      |
| `biblioteca/templates/biblioteca/por_autor.html` | Template por autor                        | 7      |

**Total: 120 puntos**

### 4. Comprobar que funciona

```bash
python manage.py runserver
```

Visita en el navegador:

- http://127.0.0.1:8000/biblioteca/autor/1/libros/

> El proyecto debe arrancar **sin errores** antes y después de tus cambios.
> Usa `python manage.py check` para comprobarlo rápidamente.
