from django import forms
from lineaBase.models import LineaBase
from item.models import Item
import django_filters


class add_lb_form(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), required=False)
    class Meta:
        model=LineaBase
        exclude=['estado','fase']

class LBFilter(django_filters.FilterSet):
    class Meta:
        model = LineaBase
        fields = ['descripcion']


class edit_lb_form(forms.ModelForm):

    class Meta:
        model=LineaBase
        exclude=['estado','fase',"items"]
