from solicitudCambio.models import Solicitud
from django import forms

__author__ = 'ccaballero'


class CrearSolicitudForm (forms.modelForm):

    class Meta:
        model = Solicitud
        fields = ['item', 'fecha_caducar', 'motivo']