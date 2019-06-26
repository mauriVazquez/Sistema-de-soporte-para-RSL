from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.http import Http404, HttpResponseRedirect

from docx import Document
from docx.shared import Inches
import os

from .models import *
from .forms import * 

@login_required
def nueva_revision(request):


    if request.method == 'POST':
        revision_form = RevisionForm(request.POST)

        print(request.POST)
        if revision_form.is_valid():
            
            investigador = Investigador.objects.get(usuario__username = request.user)
            revision_form.save()
            revision = Revision.objects.latest('pk')

            for x in range((int(request.POST['preguntas-TOTAL_FORMS']))):
                if request.POST['pregunta-'+str(x)] != "":
                    pregunta = PreguntaDeInvestigacion()
                    pregunta.revision = revision
                    pregunta.pregunta = request.POST['pregunta-'+str(x)]
                    pregunta.save()

            for x in range((int(request.POST['criterios-TOTAL_FORMS']))):
                if request.POST['criterio-'+str(x)+'-descripcion'] != "BORRAR":
                    criterio = Criterio()
                    criterio.descripcion = request.POST['criterio-'+str(x)+'-descripcion']
                    criterio.tipo = request.POST['criterio-'+str(x)+'-tipo']
                    criterio.revision = revision
                    criterio.save()

            modificacion = Modificacion()
            modificacion.revision = revision
            modificacion.investigador = investigador
            modificacion.descripcion = "Creación"
            modificacion.save()

            return HttpResponseRedirect('/inicio/')
        else:
            return HttpResponseRedirect('/inicio/')
    else:
        revision_form = RevisionForm()


    revisiones = Revision.objects.filter(investigadores__usuario__pk = request.user.pk)
    return render(request, 'revisiones/nueva_revision.html', {
        'revisiones':revisiones,
        'revision_form': revision_form,
    })
    

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
        preguntas = PreguntaDeInvestigacion.objects.filter(revision__pk = revision_id)
        criterios = Criterio.objects.filter(revision__pk = revision_id)
        articulos = Articulo.objects.filter(revision__pk = revision_id)
        context = {
            'revisiones':revisiones,
            'revision': revision,
            'investigadores': investigadores,
            'bibliotecas': bibliotecas,
            'metadatos': metadatos,
            'articulos': articulos,
            'preguntas': preguntas,
            'criterios': criterios,
        }
    except Revision.DoesNotExist:
        raise Http404("La revision no existe")

    return render(request, 'revisiones/detalle.html', context)


def crear_formulario(request, revision_id):

    document = Document()
    revision = Revision.objects.get(pk=revision_id)

    if not os.path.exists('media/'+str(revision_id)):
        os.makedirs('media/'+str(revision_id))

    document.save('media/'+str(revision_id)+'/Formulario de extraccion.docx')

    return HttpResponseRedirect('/revisiones/'+ str(revision_id))
