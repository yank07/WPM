__author__ = 'rodrigo'

from django import forms
from principal.models import UserProfile, Proyecto, EstadosProyecto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User


class UserProfileForm (forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['direccion', 'telefono', 'activo']



class ProyectoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    presupuesto = forms.IntegerField()
    observaciones = forms.CharField(max_length=200)
    estado = forms.ModelChoiceField(queryset=EstadosProyecto.objects.all())

    class Meta:
        model = Proyecto
        fields = ['usuario', 'nombre', 'presupuesto', 'observaciones']


