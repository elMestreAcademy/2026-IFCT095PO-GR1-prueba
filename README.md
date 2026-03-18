# Examen práctico - IFCT095PO · Python y Django

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

| Archivo                                          | Ejercicio                                         | Puntos |
| ------------------------------------------------ | ------------------------------------------------- | ------ |
| `biblioteca/models.py`                           | Modelo `Resena` + registro en admin               | 20     |
| `biblioteca/admin.py`                            | Registrar `Resena` en el panel de administración   | (incl) |
| `biblioteca/urls.py`                             | Ruta `libro/<int:libro_id>/resenas/`               | 3      |
| `biblioteca/views.py`                            | Vista `resenas_libro`                              | 10     |
| `biblioteca/templates/biblioteca/resenas.html`   | Template de reseñas de un libro                    | 7      |
| `biblioteca/forms.py`                            | `ResenaForm` con validaciones personalizadas       | 20     |

**Total: 60 puntos (parte práctica)**

### 4. Comprobar que funciona

```bash
python manage.py runserver
```

Visita en el navegador:

- http://127.0.0.1:8000/libro/1/resenas/

> El proyecto debe arrancar **sin errores** antes y después de tus cambios.
> Usa `python manage.py check` para comprobarlo rápidamente.
