from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioReceta
from .models import Receta

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