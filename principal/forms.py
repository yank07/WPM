__author__ = 'rodrigo'

from django import forms
from principal.models import UserProfile, Proyecto
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

    class Meta:
        model = Proyecto
        fields = ['usuario', 'nombre', 'presupuesto', 'observaciones']