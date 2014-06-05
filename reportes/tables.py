from django.contrib.auth.models import User
from item.models import Item
from proyecto.models import Fase
from solicitudCambio.models import Solicitud

__author__ = 'ccaballero'
import django_tables2 as tables


class SolicitudReporteTable(tables.Table):

    class Meta:
        model = Solicitud
        col_attrs = {"class": "text-right"}
        attrs = {"class": "paleblue"}
        fields = ("motivo", "item", "impacto", "estado")
        sequence = ("motivo", "item", "impacto", "estado")


class UsuariosReporteTable(tables.Table):

    class Meta:
        model = User
        attrs = {"class": "paleblue"}
        fields = ("username", "first_name", "last_name")
        sequence = ("username", "first_name", "last_name")


class FaseReporteTable(tables.Table):

    class Meta:
        model = Fase
        attrs = {"class": "paleblue"}
        fields = ("id", "nombre")
        sequence = ("id", "nombre")


class ItemReporteTable(tables.Table):

    class Meta:
        model = Item
        attrs = {"class": "paleblue"}
        fields = ("nombre", "tipoitem", "estado", "descripcion", "version", "complejidad", "costo",
                  "fecha_creacion", "fecha_modificacion")
        sequence = ("nombre", "tipoitem", "estado", "descripcion", "version", "complejidad", "costo",
                    "fecha_creacion", "fecha_modificacion")


class ItemVersionReporteTable(tables.Table):

    class Meta:
        model = Item
        attrs = {"class": "paleblue"}
        fields = ("nombre", "estado", "descripcion", "version", "complejidad", "costo",
                  "fecha_creacion", "fecha_modificacion")
        sequence = ("nombre", "estado", "descripcion", "version", "complejidad", "costo",
                  "fecha_creacion", "fecha_modificacion")