from django import forms
from .models import Receta, Calificacion

class FormularioReceta(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'ingredientes', 'pasos', 'tiempo', 'categoria', 'imagen']
        labels = {
            'titulo': 'Título de la receta',
            'ingredientes': 'Ingredientes',
            'pasos': 'Pasos de preparación',
            'tiempo': 'Tiempo (minutos)',
            'categoria': 'Categoría',
            'imagen': 'Imagen de la receta',
        }
        widgets = {
            'ingredientes': forms.Textarea(attrs={'rows': 3}),
            'pasos': forms.Textarea(attrs={'rows': 4}),
        }

class FormularioCalificacion(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['puntuacion', 'comentario']
        labels = {
            'puntuacion': 'Puntuación (1-5)',
            'comentario': 'Comentario',
        }
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 3}),
        }