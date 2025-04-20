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

    context = {
        'recetas': recetas,
        'query': query,
        # 'categoria': categoria,
        'categoria': categoria,
        'categorias': Receta.CATEGORIAS,
    }
    return render(request, 'core/index.html', context)