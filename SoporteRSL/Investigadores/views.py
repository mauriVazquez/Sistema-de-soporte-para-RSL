from django.shortcuts import render
from django.contrib.auth.decorators import login_required



from Revisiones.models import Revision
from .models import Investigador
# Create your views here.


@login_required
def inicio(request):

    revisiones = Revision.objects.filter(investigadores__usuario__pk = request.user.pk)
    investigador = Investigadores.get(usuario = request.user)

    context['revisiones'] = revisiones



    return render(request, 'inicio.html', context)
