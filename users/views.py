from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from core.views import obtener_recetas_filtradas
from recetas_app.forms import FormularioReceta
from recetas_app.models import Receta
from .forms import FormularioRegistro, FormularioInicioSesion
from django.contrib.auth.decorators import login_required

def registrar_usuario(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect('inicio')
    else:
        formulario = FormularioRegistro()
    return render(request, 'users/registrar.html', {'formulario': formulario})

def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = FormularioInicioSesion(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            return redirect('inicio')
    else:
        formulario = FormularioInicioSesion()
    return render(request, 'users/iniciar_sesion.html', {'formulario': formulario})

def cerrar_sesion(request):
    logout(request)
    return redirect('pagina_principal')

# @login_required
# def inicio(request):
#     return render(request, 'users/inicio.html')

@login_required
def inicio(request):
    query = request.GET.get('q', '')
    categoria = request.GET.get('categoria', '')
    recetas = obtener_recetas_filtradas(query, categoria)

    formulario = None
    if request.user.is_superuser and request.method == 'POST':
        formulario = FormularioReceta(request.POST, request.FILES)
        if formulario.is_valid():
            receta = formulario.save(commit=False)
            receta.usuario = request.user
            receta.save()
            return redirect('inicio')
    elif request.user.is_superuser:
        formulario = FormularioReceta()

    return render(request, 'users/inicio.html', {
        'recetas': recetas,
        'formulario': formulario,
        'query': query,
        # 'categoria': categoria,
        'categoria': categoria,
        'categorias': Receta.CATEGORIAS,
    })