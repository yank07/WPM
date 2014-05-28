__author__ = 'ccaballero'

import django_tables2 as tables
from models import Solicitud, Comite


class SolicitudTable(tables.Table):

    acciones = tables.TemplateColumn(template_name='columna_sc.html')

    class Meta:
        model = Solicitud
        attrs = {"class": "paleblue"}
        fields = ("motivo", "item", "impacto", "estado")
        sequence = ("motivo", "item", "impacto", "estado")


class MisSolicitudesTable(tables.Table):
    acciones = tables.TemplateColumn(template_name='column_sc.html')

    class Meta:
        model = Solicitud
        attrs = {"class": "paleblue"}
        fields = ("motivo", "item", "impacto", "estado")
        sequence = ("motivo", "item", "impacto", "estado")



class admin_comite_table(tables.Table):
    #nombre = tables.Column(verbose_name="Nombre del comite")
    my_column = tables.TemplateColumn(verbose_name=('Editar'),
                                      template_name='column_comite.html',
                                      sortable=False)

    class Meta:
        model = Comite
        attrs = {"class": "paleblue"}
        fields = ("proyecto", "primer_integrante" , "segundo_integrante", "tercer_integrante", "estado")
        sequence = ("proyecto", "primer_integrante" , "segundo_integrante", "tercer_integrante", "estado")