from django import forms
from .models import Receta

class FormularioReceta(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'ingredientes', 'pasos', 'tiempo', 'etiquetas']
        labels = {
            'titulo': 'Título de la receta',
            'ingredientes': 'Ingredientes',
            'pasos': 'Pasos de preparación',
            'tiempo': 'Tiempo (minutos)',
            'etiquetas': 'Etiquetas (opcional)',
        }
        widgets = {
            'ingredientes': forms.Textarea(attrs={'rows': 3}),
            'pasos': forms.Textarea(attrs={'rows': 4}),
        }
