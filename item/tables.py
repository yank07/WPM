import django_tables2 as tables
from item.models import Item
from proyecto.models import Fase


class ItemTable(tables.Table):
    nombre = tables.Column(verbose_name="Nombre del item")
    my_column = tables.TemplateColumn(verbose_name=('Editar'),
                                    template_code='<a href="/item/asignar_valor_item/{{ record.id }}"><input class="btn btn-xs btn-default" type="submit" name="submit" value="Ver Atributos" /></a>',
                                    sortable=False)
    class Meta:
        model = Item
        attrs = {"class": "paleblue"}
        fields = ("nombre", "id","complejidad","costo","estado")
        sequence = ("nombre", "id","complejidad","costo","estado")
