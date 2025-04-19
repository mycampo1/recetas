from django.db import models
from django.conf import settings

class Receta(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recetas')
    titulo = models.CharField(max_length=255)
    ingredientes = models.TextField()
    pasos = models.TextField()
    tiempo = models.PositiveIntegerField(help_text="Tiempo en minutos")
    etiquetas = models.CharField(max_length=255, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
