import django_tables2 as tables
from lineaBase.models import LineaBase
from proyecto.models import Fase
from item.models import Item


class LBTable(tables.Table):
    #nombre = tables.Column(verbose_name="Nombre del item")
    my_column = tables.TemplateColumn(verbose_name=('Ver Items'),
                                    template_name='columna_item_lb.html',
                                    sortable=False)


    class Meta:
        model = LineaBase
        attrs = {"class": "paleblue"}
        fields = ( "id","descripcion","fase","estado")
        sequence = ( "id","descripcion","fase","estado")


class ItemTable(tables.Table):
    nombre = tables.Column(verbose_name="Nombre del item")

    class Meta:
        model = Item
        attrs = {"class": "paleblue"}
        fields = ("nombre", "id","complejidad","costo","estado","version")
        sequence = ("nombre", "id","complejidad","costo","estado","version")
