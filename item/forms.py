from django import forms
import django_filters
from eav.models import Attribute, Value
from TipoItemApp.models import TipoItem
from item.models import Item
from proyecto.models import Fase

class add_item_form(forms.ModelForm):
    """
    Form para crear items
    """
    # def __init__(self, *args, **kwargs):
    #     id_f = kwargs.pop('id_fase')
    #     super(add_item_form, self).__init__(*args, **kwargs)
    #     self.fields['id_fase'] = id_f
    #     self.fields['tipoitem'].queryset = TipoItem.objects.filter(fases__id=self.fields['id_fase'])

    tipoitem = forms.ModelChoiceField(queryset=TipoItem.objects.all())

    class Meta:
        model=Item
        exclude=['fecha_creacion','fecha_modificacion','estado','id_item','version']


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
                self.fields[attr.name] = forms.BooleanField(label=attr.name+'('+attr.datatype+')',required=attr.required)

class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['nombre']
