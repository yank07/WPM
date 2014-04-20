__author__ = 'rodrigo'
from proyecto.models import Proyecto, Fase
from django import forms
import django_filters


class ProyectoForm(forms.ModelForm):
    """
    Form para agregar proyecto
    """
    nombre = forms.CharField(max_length=50)
    presupuesto = forms.IntegerField()
    observaciones = forms.CharField(max_length=200)


    class Meta:
        model = Proyecto
        fields = ['usuario', 'nombre', 'presupuesto', 'observaciones','numero_fases','estado' ]


class ProyectoFilter(django_filters.FilterSet):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'observaciones']


class FaseForm(forms.ModelForm):
    """
    Form para modificar Fase
    """


    class Meta:
        model = Fase
        fields = [ 'nombre','proyecto']