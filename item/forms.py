from django import forms
import django_filters
from eav.models import Attribute
from TipoItemApp.models import TipoItem
from item.models import Item
from proyecto.models import Fase

class add_item_form(forms.ModelForm):
    """
    Form para crear items
    """
    #observacion=forms.CharField(required=False)
    #archivo = forms.FileField(required=False)

    class Meta:
        model=Item
        exclude=['fecha_creacion','fecha_modificacion','estado']
