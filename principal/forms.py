__author__ = 'rodrigo'

from django import forms
from principal.models import UserProfile, Proyecto, EstadosProyecto
from django.contrib.auth.models import User


class UserProfileForm (forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['direccion','telefono', 'activo']


class UserForm(forms.ModelForm):
    username= forms.CharField(help_text="")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class ProyectoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, help_text="Nombre del proyecto")
    presupuesto = forms.IntegerField(help_text="Presupuesto del Proyecto")
    observaciones = forms.CharField(max_length=200, help_text="Observaciones varias")
    estado = forms.ModelChoiceField(queryset=EstadosProyecto.objects.all())

    class Meta:
        model = Proyecto
        fields = ['usuario', 'nombre', 'presupuesto', 'observaciones']