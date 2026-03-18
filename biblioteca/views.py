from django.shortcuts import get_object_or_404, redirect, render

from .forms import LibroForm
from .models import Autor, Libro


def lista_libros(request):
    libros = Libro.objects.select_related('autor').order_by('titulo')
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros})


def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro.objects.select_related('autor').prefetch_related('autores_secundarios'), pk=libro_id)
    return render(request, 'biblioteca/detalle_libro.html', {'libro': libro})


def libros_por_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    libros = Libro.objects.filter(autor=autor, publicado__isnull=False)
    return render(
        request,
        'biblioteca/por_autor.html',
        {
            'autor': autor,
            'libros': libros,
        },
    )

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            return redirect('biblioteca:libros-por-autor', autor_id=libro.autor_id)
    else:
        form = LibroForm()
    return render(request, 'biblioteca/crear.html', {'form': form})
