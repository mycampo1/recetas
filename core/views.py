from django.shortcuts import render
from recetas_app.models import Receta
from django.db.models import Q

def pagina_principal(request):
    query = request.GET.get('q')
    recetas = Receta.objects.all()

    if query:
        recetas = recetas.filter(
            Q(titulo__icontains=query) |
            Q(etiquetas__icontains=query)
        )

    context = {
        'recetas': recetas,
        'query': query or '',
    }
    return render(request, 'core/index.html', context)
