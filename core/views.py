from django.shortcuts import render
from recetas_app.models import Receta
from django.db.models import Q

def obtener_recetas_filtradas(query, categoria):
    recetas = Receta.objects.all()
    if query:
        recetas = recetas.filter(
            Q(titulo__icontains=query) |
            Q(ingredientes__icontains=query)
        )
    if categoria:
        recetas = recetas.filter(categoria=categoria)
    return recetas

def pagina_principal(request):
    query = request.GET.get('q', '')
    categoria = request.GET.get('categoria', '')
    recetas = obtener_recetas_filtradas(query, categoria)

    # Calcular las estrellas para cada receta
    for receta in recetas:
        receta.estrellas = []
        puntuacion = receta.puntuacion_promedio
        for i in range(1, 6):  # Iterar de 1 a 5
            if i <= puntuacion:
                receta.estrellas.append('llena')  # Estrella llena
            elif i - 1 < puntuacion < i:
                receta.estrellas.append('media')  # Estrella medio llena
            else:
                receta.estrellas.append('vacia')  # Estrella vacía

    context = {
        'recetas': recetas,
        'query': query,
        'categoria': categoria,
        'categorias': Receta.CATEGORIAS,
    }
    return render(request, 'core/index.html', context)