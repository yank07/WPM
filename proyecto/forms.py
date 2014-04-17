__author__ = 'rodrigo'
from proyecto.models import Proyecto
from django import forms

class ProyectoForm(forms.ModelForm):
    """
    Form para agregar proyecto
    """
    nombre = forms.CharField(max_length=50)
    presupuesto = forms.IntegerField()
    observaciones = forms.CharField(max_length=200)


    class Meta:
        model = Proyecto
        fields = ['usuario', 'nombre', 'presupuesto', 'observaciones','numero_fases','estado']
