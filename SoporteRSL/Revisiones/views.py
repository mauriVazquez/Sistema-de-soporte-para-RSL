from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.http import Http404, HttpResponseRedirect

from .models import *
from .forms import * 

@login_required
def nueva_revision(request):
    PreguntaDeInvestigacionFormset = modelformset_factory(PreguntaDeInvestigacion,fields=('pregunta',))
    CriterioFormset = modelformset_factory(Criterio, fields=('tipo', 'descripcion'))    
    if request.method == 'POST':
        
        revision_form = RevisionForm(request.POST)
        preguntas_formset = PreguntaDeInvestigacionFormset(request.POST, prefix='preguntas')
        print(preguntas_formset)
        criterio_formset = CriterioFormset(request.POST, prefix='criterios')
        if preguntas_formset.is_valid() and revision_form.is_valid() and criterio_formset.is_valid():
            
            revision_form.save()
            revision = Revision.objects.latest('pk')
            preguntas_formset.save(commit = False)
            criterio_formset.save(commit = False)

            for pregunta in preguntas_formset:    
                pregunta.revision = revision.pk

            for criterio in criterio_formset:    
                criterio.revision = revision.pk

            preguntas_formset.save()
            criterio_formset.save()
            
            return HttpResponseRedirect('/inicio/')

    else:
        revision_form = RevisionForm()
        preguntas_formset = PreguntaDeInvestigacionFormset(prefix='preguntas')
        criterio_formset = CriterioFormset(prefix='criterios')

    revisiones = Revision.objects.filter(investigadores__usuario__pk = request.user.pk)
    context = {
        'revisiones':revisiones,
        'revision_form': revision_form,
        'criterio_formset': criterio_formset,
        'preguntas_formset': preguntas_formset
    }
    return render(request, 'revisiones/nueva_revision.html', context)
    

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
        articulos = Articulo.objects.filter(revision__pk = revision_id)
        context = {
            'revisiones':revisiones,
            'revision': revision,
            'investigadores': investigadores,
            'bibliotecas': bibliotecas,
            'metadatos': metadatos,
            'articulos': articulos
        }
    except Revision.DoesNotExist:
        raise Http404("La revision no existe")

    return render(request, 'revisiones/detalle.html', context)