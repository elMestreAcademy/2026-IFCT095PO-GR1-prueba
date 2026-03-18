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
