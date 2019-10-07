from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from docx import Document
from docx.shared import Inches
import os

from .models import *
from .forms import RevisionForm, MetadatosForm, RevisionFormInicial

@login_required
def nueva_revision(request):

    if request.method == 'POST':
        revision_form = RevisionForm(request.POST)

        print(request.POST)
        if revision_form.is_valid():

            investigador = Investigador.objects.get(usuario__username = request.user)
            revision = get_object_or_404(Revision, pk=request.POST.get('id_revison',0))

            PreguntaDeInvestigacion.objects.filter(revision__pk =request.POST.get('id_revison',0)).delete()

            for x in range((int(request.POST['preguntas-TOTAL_FORMS']))):
                if request.POST.get('pregunta-'+str(x),False) != "BORRAR" and request.POST.get('pregunta-'+str(x),False) != "":
                    pregunta = PreguntaDeInvestigacion()
                    pregunta.revision = revision
                    pregunta.pregunta = request.POST.get('pregunta-'+str(x),False)
                    pregunta.save()

            revision.metadatos.clear()
            lista_metadatos = request.POST.getlist('metadatos')             
            for metadato in lista_metadatos:
                revision.metadatos.add(Metadato.objects.get(pk=metadato))
            
            lista_bibliotecas = request.POST.getlist('bibliotecas')
            revision.bibliotecas.clear()
            for biblioteca in lista_bibliotecas:
                revision.bibliotecas.add(Biblioteca.objects.get(pk=biblioteca))
            
            revision.cadena_de_busqueda = request.POST['cadena_de_busqueda']

            Criterio.objects.filter(revision__pk =request.POST.get('id_revison',0)).delete()

            for x in range(1,(int(request.POST['criterios-TOTAL_FORMS']))):
                if request.POST.get('id_criterio-'+str(x)+'-descripcion') != "BORRAR":
                    criterio = Criterio()
                    criterio.descripcion = request.POST.get('id_criterio-'+str(x)+'-descripcion')
                    criterio.tipo = request.POST.get('id_criterio-'+str(x)+'-tipo')
                    criterio.revision = revision
                    criterio.save()

            revision.save()

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

@login_required                
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
        revision_form = RevisionFormInicial()

    revisiones = Revision.objects.filter(investigadores__usuario__pk = request.user.pk)
    context = {
        'revisiones':revisiones,
        'revision_form': revision_form,
    }
    
    
    return render(request, 'revisiones/comenzar_revision.html', context)


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
        revision_form = RevisionForm(instance=revision)
        
        investigadores = Investigador.objects.filter(revision__pk = revision_id)
        preguntas = PreguntaDeInvestigacion.objects.filter(revision__pk = revision_id)
        criterios = Criterio.objects.filter(revision__pk = revision_id)
        articulos = Articulo.objects.filter(revision__pk = revision_id)
        context = {
            'revisiones':revisiones,
            'revision': revision,
            'investigadores': investigadores,
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

    document = Document('media/Template of the Data Extraction Form.docx')
    
    revision = Revision.objects.get(pk=revision_id)
    
    table = document.add_table(rows=0, cols=2)
    table.style = 'estilo template'

    for i in range(1,(int(request.POST.get('cant-campos',0))+1)):
        if (request.POST.get('campo-'+str(i), 'campo no existente') != "BORRAR"):
            row = table.add_row()
            row.cells[0].text = request.POST.get('campo-'+str(i), 'campo no existente')
            

    if not os.path.exists('media/'+str(revision_id)):
        os.makedirs('media/'+str(revision_id))
    
    documento_creado = True

    document.save('media/'+str(revision_id)+'/Formulario de extraccion.docx')
    revision.formulario_generico = True
    revision.save()
    #return HttpResponseRedirect('/revisiones/'+ str(revision_id))
    return JsonResponse({'documento_creado': documento_creado})

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