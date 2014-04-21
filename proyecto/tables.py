import django_tables2 as tables
from proyecto.models import Proyecto, Fase
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




