from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from Revisiones.models import Revision


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

    
