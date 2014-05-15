import django_tables2 as tables
from proyecto.models import Proyecto, Fase
from item.models import Item
from django_tables2.utils import A




class ProyectoTable(tables.Table):
    nombre = tables.Column(verbose_name="Nombre del proyecto")
    my_column = tables.TemplateColumn(verbose_name=('Editar'),
                                    template_name='my_column.html',
                                    sortable=False)

    class Meta:
        model = Proyecto
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
        fields = ("nombre", "observaciones" , "estado", "numero_fases", "presupuesto" , "usuario" ,"id")
        sequence = ("nombre", "observaciones", "estado", "numero_fases", "presupuesto" , "usuario", "id")



class FasesTable(tables.Table):
    nombre = tables.Column(verbose_name="Nombre de la Fase")
    my_column = tables.TemplateColumn(verbose_name=('Editar'),
                                    template_name='columna_fase.html',
                                    sortable=False)
    class Meta:
        model = Fase
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
        fields = ("nombre", "proyecto","id")
        sequence = ("nombre", "proyecto", "id")


class ProyectoDashboardTable(tables.Table):
    nombre = tables.Column(verbose_name="Nombre del Proyecto")
    columna = tables.TemplateColumn(verbose_name=('Ver'), template_name='my_column.html', sortable=False)

    class Meta:
        model = Proyecto
        attrs = {"class": "paleblue"}
        fields = ("nombre", "observaciones" , "estado", "numero_fases", "presupuesto" , "usuario")
        sequence = ("nombre", "observaciones", "estado", "numero_fases", "presupuesto" , "usuario")


class ListaItemTable(tables.Table):
    nombre = tables.Column(verbose_name='Nombre del Item')

    class Meta:
        model = Item
        attrs = {"class": "paleblue"}
        fields = ("id", "nombre", "tipoitem", "fase", "complejidad", "costo", "estado", "descripcion", "archivo")
        sequence = ("id", "nombre", "tipoitem", "fase", "complejidad", "costo", "estado", "descripcion", "archivo")