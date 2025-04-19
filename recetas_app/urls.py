from django.urls import path
from .views import agregar_receta

urlpatterns = [
    path('agregar/', agregar_receta, name='agregar_receta'),
]
