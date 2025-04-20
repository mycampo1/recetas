from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FormularioReceta, FormularioCalificacion
from .models import Receta, Calificacion

@login_required
def agregar_receta(request):
    if request.method == 'POST':
        formulario = FormularioReceta(request.POST, request.FILES)  # Manejar archivos
        if formulario.is_valid():
            receta = formulario.save(commit=False)
            receta.usuario = request.user
            receta.save()
            return redirect('inicio')  # o a una vista de detalle o lista
    else:
        formulario = FormularioReceta()
    return render(request, 'recetas_app/agregar_receta.html', {'formulario': formulario})

@login_required
def calificar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        formulario = FormularioCalificacion(request.POST)
        if formulario.is_valid():
            calificacion = formulario.save(commit=False)
            calificacion.receta = receta
            calificacion.usuario = request.user
            calificacion.save()
            return redirect('detalle_receta', receta_id=receta.id)  # Cambia 'detalle_receta' por tu vista de detalle
    else:
        formulario = FormularioCalificacion()
    return render(request, 'recetas_app/calificar_receta.html', {'receta': receta, 'formulario': formulario})