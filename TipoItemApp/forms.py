import django_filters
from eav.models import Attribute
from TipoItemApp.models import TipoItem
from proyecto.models import Fase

__author__ = 'roquegv'

from django import forms


class add_tipoitem_form(forms.ModelForm):
    """
    Form para crear tipos de items
    """
    observacion = forms.CharField(required=False)
    #atributos = forms.ModelMultipleChoiceField(required=False)
    class Meta:
        model = TipoItem
        widgets = {'atributos': forms.SelectMultiple(attrs={'size':'10'})}
        fields = ['nombre','descripcion','observacion','atributos','fases']


class add_atributo_form(forms.Form):
    """
    Form para crear los atributos de los tipos de items
    """
    tipos = (
            ('int','Entero'),
            ('float','Decimal'),
            ('text','Texto'),
            ('bool','Boolean'),
            ('date','Fecha')
        )
    tipo_item = forms.ModelChoiceField(queryset=TipoItem.objects.all(),required=False)
    nombre_atributo = forms.CharField(max_length=50)
    tipo = forms.ChoiceField(choices=tipos)
    obligatorio = forms.BooleanField(required=False)


class edit_atributo_form(forms.Form):
    """
    Form para crear los atributos de los tipos de items
    """
    tipos = (
            ('int','Entero'),
            ('float','Decimal'),
            ('text','Texto'),
            ('bool','Boolean'),
            ('date','Fecha')
        )
    nombre = forms.CharField(max_length=50)
    tipo = forms.ChoiceField(choices=tipos)
    obligatorio = forms.BooleanField(required=False)

class listar_atributos_form(forms.Form):
    """
    Form para listar los atributos por tipo de item
    """
    nombre = forms.ModelChoiceField(queryset=TipoItem.objects.all(),help_text='Nombre de tipo de item')

class delete_tipoitem_form(forms.Form):
    """
    Form para listar los atributos por tipo de item
    """
    nombre = forms.ModelChoiceField(queryset=TipoItem.objects.all(),help_text='Nombre de tipo de item')

class delete_atributo_form(forms.Form):
    """
    Form para listar los atributos por tipo de item
    """
    nombre = forms.ModelChoiceField(queryset=Attribute.objects.all(),help_text='Nombre de atributo')

class importar_tipooitem_form(forms.Form):
    tipoitem = forms.ModelChoiceField(queryset=TipoItem.objects.all(),help_text='Nombre de tipo de item')
    fase = forms.ModelChoiceField(queryset=Fase.objects.all(),help_text='Nombre de Fase')


class TipoItemFilter(django_filters.FilterSet):
    class Meta:
        model = TipoItem
        fields = ['nombre', 'descripcion']

class AtributoFilter(django_filters.FilterSet):
    class Meta:
        model = Attribute
        fields = ['name', 'datatype']