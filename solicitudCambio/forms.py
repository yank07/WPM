from django import forms
import django_filters
from solicitudCambio.models import Solicitud, Comite


__author__ = 'ccaballero'


class CrearSolicitudForm (forms.ModelForm):
    fecha_caducar = forms.DateField()
    motivo = forms.CharField(max_length=200)

    class Meta:
        model = Solicitud
        fields = ['fecha_caducar', 'motivo']


class crear_comite_form(forms.ModelForm):
    """
    Form para crear comite
    """
    #proyecto = forms.ModelChoiceField(Proyecto.objects.none(),widget=forms.HiddenInput)
    class Meta:
        model=Comite
        #exclude=['proyecto']


class comite_filter(django_filters.FilterSet):
    class Meta:
        model = Comite
        fields = ['proyecto']


class SolicitudFilter(django_filters.FilterSet):

    class Meta:
        model = Solicitud
        fields = ['motivo', 'item']