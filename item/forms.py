from django import forms
import django_filters
from eav.models import Attribute, Value
from TipoItemApp.models import TipoItem
from item.models import Item, relaciones
from proyecto.models import Fase

class add_item_form(forms.ModelForm):
    """
    Form para crear items
    """
    tipoitem = forms.ModelChoiceField(queryset=TipoItem.objects.all())
    antecesor = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), required=False)
    padre = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), required=False)
    class Meta:
        model=Item
        exclude=['fecha_creacion','fecha_modificacion','estado','id_item','version','rango_valor_inicio','rango_valor_final']

class asignar_valor_item_form(forms.Form):
    """
    Form para asignar valores a los atributos de un item
    """
    def __init__(self, *args, **kwargs):
        attrs = kwargs.pop('atributos')
        super(asignar_valor_item_form, self).__init__(*args, **kwargs)
        for attr in attrs:
            if attr.datatype == 'int':
                self.fields[attr.name] = forms.IntegerField(label=attr.name+'('+attr.datatype+')',required=attr.required)
            if attr.datatype == 'float':
                self.fields[attr.name] = forms.DecimalField(label=attr.name+'('+attr.datatype+')',required=attr.required)
            if attr.datatype == 'date':
                self.fields[attr.name] = forms.DateField(label=attr.name+'('+attr.datatype+')',required=attr.required,
                                                         show_hidden_initial='2014-01-01')
            if attr.datatype == 'text':
                self.fields[attr.name] = forms.CharField(label=attr.name+'('+attr.datatype+')',required=attr.required)
            if attr.datatype == 'bool':
                self.fields[attr.name] = forms.BooleanField(label=attr.name+'('+attr.datatype+')',required=False)

class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['nombre']

class edit_item_form(forms.ModelForm):
    """
    Form para editar item
    """
    ESTADOS_CHOICES = (
        ('ACT','Activo'),
        ('REV','Revision'),
        ('APROB','Aprobado'),
        ('ELIM','Eliminado')
    )
    estado = forms.ChoiceField(ESTADOS_CHOICES)
    class Meta:
        model=Item
        fields=['complejidad','costo','estado','descripcion','observacion','archivo']

class crear_sucesor_form(forms.Form):
    """
    Form para crear relacion Sucesor entre fases adyacentes
    """
    items_origen = forms.ModelChoiceField(queryset=Item.history.all())
    items_destino = forms.ModelChoiceField(queryset=Item.history.all())

class delete_relacion_form(forms.Form):
    """
    Form para editar las relaciones de un item
    """
    relacion = forms.ModelChoiceField(queryset=relaciones.objects.all())