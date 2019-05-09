from django.shortcuts import render
from django.contrib.auth.decorators import login_required



from Revisiones.models import Revision
from .models import Investigador
# Create your views here.


@login_required
def inicio(request):

    revisiones = Revision.objects.filter(investigadores__usuario__pk = request.user.pk)
    investigador = Investigador.objects.get(usuario__username = request.user)

    revisiones_lista = []

    for r in revisiones:
        dic = {}
        dic['id'] = r.pk
        dic['titulo'] = r.titulo,
        revisiones_lista.append(dic)
    
    context = {
            "title" : 'Revisiones',
            "revisiones" : revisiones,
            "datos_r" : revisiones_lista
            }

    return render(request, 'Investigadores/inicio.html', context)
