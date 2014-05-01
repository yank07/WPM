import django_tables2 as tables
from item.models import Item
from proyecto.models import Fase


class ItemTable(tables.Table):
    nombre = tables.Column(verbose_name="Nombre del item")
    my_column = tables.TemplateColumn(verbose_name=('Editar'),
                                    template_name='columna_item.html',
                                    sortable=False)
    class Meta:
        model = Item
        attrs = {"class": "paleblue"}
        fields = ("nombre", "id","complejidad","costo","estado","version","archivo")
        sequence = ("nombre", "id","complejidad","costo","estado","version","archivo")

class RevivirItemTable(tables.Table):
    nombre = tables.Column(verbose_name="Nombre del item")
    my_column = tables.TemplateColumn(verbose_name=('Editar'),
                                    template_code='<a href="/item/revivir_item/{{ record.id }}"><input class="btn btn-xs btn-default" type="submit" name="submit" value="Revivir" /></a>',
                                    sortable=False)
    class Meta:
        model = Item
        attrs = {"class": "paleblue"}
        fields = ("nombre", "id","complejidad","costo","estado","version","archivo")
        sequence = ("nombre", "id","complejidad","costo","estado","version","archivo")