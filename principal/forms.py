__author__ = 'rodrigo'

from django import forms
from principal.models import UserProfile
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    """
    Form para agregar usuario
    """
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User


class UserProfileForm (forms.ModelForm):
    """
    Form para agregar perfil de usuario
    """

    class Meta:
        model = UserProfile
        fields = ['direccion', 'telefono', 'activo']




class RolForm(forms.ModelForm):
    """
    Form para agregar un rol nuevo
    """
    class Meta:
        model = Group
        widgets = {'permissions': forms.SelectMultiple(attrs={'size':'10'})}
        fields = ['permissions', 'name']

class asignarForm(forms.Form):
    """
    Form para asignar roles a un usuario
    """
    #roles = forms.ModelMultipleChoiceField(Rol.objects.all())
    #usuarios = forms.ModelChoiceField(User.objects.all())
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all())
    username = forms.ModelChoiceField(queryset=User.objects.all())

