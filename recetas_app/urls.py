from django.urls import path
from .views import agregar_receta, calificar_receta, detalle_receta

urlpatterns = [
    path('agregar/', agregar_receta, name='agregar_receta'),
    path('calificar/<int:receta_id>/', calificar_receta, name='calificar_receta'),
    path('detalle/<int:receta_id>/', detalle_receta, name='detalle_receta'),
]
