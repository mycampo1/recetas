from django.db import models
from django.conf import settings

class Receta(models.Model):
    CATEGORIAS = [
        ('saladas', 'Saladas'),
        ('vegetariana', 'Vegetariana'),
        ('especiales', 'Especiales'),
        ('postres', 'Postres'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recetas')
    titulo = models.CharField(max_length=255)
    ingredientes = models.TextField()
    pasos = models.TextField()
    tiempo = models.PositiveIntegerField(help_text="Tiempo en minutos")
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='saladas')  # Nuevo campo
    creado_en = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='recetas_imagenes/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Calificacion(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='calificaciones')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    puntuacion = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])  # Calificación de 1 a 5
    comentario = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.receta} - {self.puntuacion}"