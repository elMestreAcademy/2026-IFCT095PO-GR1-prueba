from django.contrib import admin

from .models import Autor, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'email')
    ordering = ('nombre',)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'precio', 'precio_con_iva', 'publicado')
    list_filter = ('publicado', 'autor')
    search_fields = ('titulo', 'autor__nombre')
    ordering = ('titulo',)
    date_hierarchy = 'publicado'
    filter_horizontal = ('autores_secundarios',)
    autocomplete_fields = ('autor',)
