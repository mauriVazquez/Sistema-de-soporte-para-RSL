from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse

from docx import Document
from docx.shared import Inches
import os

from .models import *
from .forms import RevisionForm, MetadatosForm

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
                if request.POST['pregunta-'+str(x)] != "BORRAR":
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
            modificacion.descripcion = "Nueva informacion de actividad 1 añadida"
            modificacion.save()

            return HttpResponseRedirect('/inicio/')
        else:
            return HttpResponseRedirect('/inicio/')
    else:        
        print(request)
        revisiones = Revision.objects.filter(investigadores__usuario__pk = request.user.pk)
        return render(request, 'revisiones/nueva_revision.html', {
            'revisiones':revisiones,
            'revision_form': revision_form,
        })
                
def comenzar_revision(request):

    if request.method == 'POST':
        
        print(request.POST)
        
        revision = Revision()
        investigador = Investigador.objects.get(usuario__username = request.user)

        revision.meta_de_necesidad_de_informacion = request.POST['meta_de_necesidad_de_informacion']
        revision.titulo = request.POST['titulo']
        revision.save()

        for i in request.POST['investigadores']:
            revision.investigadores.add(Investigador.objects.get(pk=i))

        modificacion = Modificacion()
        modificacion.revision = revision
        modificacion.investigador = investigador
        modificacion.descripcion = "Creación"
        modificacion.save()

        return HttpResponseRedirect('/inicio/')
    else:
        revision_form = RevisionForm()

    revisiones = Revision.objects.filter(investigadores__usuario__pk = request.user.pk)
    return render(request, 'revisiones/comenzar_revision.html', {
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
        
        revision_form = RevisionForm()
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
            'revision_form': revision_form,
        }
    
    
    except Revision.DoesNotExist:
        raise Http404("La revision no existe")

    if revision.estado == 'Actividad 1':
        
        return render(request, 'revisiones/nueva_revision.html', context)
    else:
        return render(request, 'revisiones/detalle.html', context)

@csrf_exempt
def crear_formulario(request, revision_id):

    document = Document()
    print(request.POST)
    revision = Revision.objects.get(pk=revision_id)

    #if not os.path.exists('media/'+str(revision_id)):
    #    os.makedirs('media/'+str(revision_id))

    #document.save('media/'+str(revision_id)+'/Formulario de extraccion.docx')
    nada = "nada"
    #return HttpResponseRedirect('/revisiones/'+ str(revision_id))
    return JsonResponse({'nada': nada})

def ayuda(request):
    revisiones = Revision.objects.filter(investigadores__usuario__pk = request.user.pk)
    context = {
            'revisiones':revisiones,
        }


    return render(request, 'SoporteRSL/ayuda.html', context)

def actividad_1(request):

    revisiones = Revision.objects.filter(investigadores__usuario__pk = request.user.pk)
    context = {
            'revisiones':revisiones,
        }

    return render(request, 'SoporteRSL/actividades/actividad_1.html', context)

def actividad_2(request):
    
    revisiones = Revision.objects.filter(investigadores__usuario__pk = request.user.pk)
    context = {
            'revisiones':revisiones,
        }

    return render(request, 'SoporteRSL/actividades/actividad_2.html', context)

def actividad_3(request):
    
    revisiones = Revision.objects.filter(investigadores__usuario__pk = request.user.pk)
    context = {
            'revisiones':revisiones,
        }

    return render(request, 'SoporteRSL/actividades/actividad_3.html', context)