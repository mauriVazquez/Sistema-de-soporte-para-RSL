from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from Revisiones.models import Revision,Biblioteca,Metadato
from Investigadores.models import Investigador


@method_decorator(login_required, name='dispatch')
class RevisionCreateView(CreateView):
    model = Revision

    fields = ['titulo',
    'meta_de_necesidad_de_informacion',
    'investigadores',
    'cadena_de_busqueda',
    'metadatos',
    'bibliotecas',
    'prueba_piloto']
    success_url = "../inicio/"

    
@login_required
def detalle(request, revision_id):
    try:
        revisiones = Revision.objects.filter(investigadores__usuario__pk = request.user.pk)
        
        revision = Revision.objects.get(pk=revision_id)
        investigadores = Investigador.objects.filter(revision__pk = revision_id)
        bibliotecas = Biblioteca.objects.filter(revision__pk = revision_id)
        metadatos = Metadato.objects.filter(revision__pk = revision_id)
        
        context = {
            'revisiones':revisiones,
            'revision': revision,
            'investigadores': investigadores,
            'bibliotecas': bibliotecas,
            'metadatos': metadatos,
        }

    except Revision.DoesNotExist:
        raise Http404("La revision no existe")

    return render(request, 'revisiones/detalle.html', context)