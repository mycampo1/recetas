from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from recetas_app.forms import FormularioReceta
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
    return redirect('iniciar_sesion')

# @login_required
# def inicio(request):
#     return render(request, 'users/inicio.html')


@login_required
def inicio(request):
    if request.method == 'POST':
        formulario = FormularioReceta(request.POST, request.FILES)  # Manejar archivos
        if formulario.is_valid():
            receta = formulario.save(commit=False)
            receta.usuario = request.user
            receta.save()
            return redirect('inicio')  # O redirigir a otra vista, como una lista de recetas
    else:
        formulario = FormularioReceta()

    return render(request, 'users/inicio.html', {'formulario': formulario})