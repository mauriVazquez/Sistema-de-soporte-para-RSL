from django import forms
from .models import Revision, PreguntaDeInvestigacion, Criterio, Articulo
from django.forms import modelformset_factory


class RevisionForm(forms.ModelForm):
     class Meta:
        model = Revision
        fields = ['titulo',
    'meta_de_necesidad_de_informacion',
    'investigadores',
    'cadena_de_busqueda',
    'metadatos',
    'bibliotecas',
    'prueba_piloto']


class PreguntaDeInvestigacionForm(forms.ModelForm):

    class Meta:
        model = PreguntaDeInvestigacion
        fields = ['pregunta']


class CriterioForm(forms.ModelForm):
    class Meta:
        model = Criterio
        fields = ['tipo','descripcion']


class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = ['titulo','archivo','leido']


