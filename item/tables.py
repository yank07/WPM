import django_tables2 as tables
from item.models import Item
from proyecto.models import Fase


class ItemTable(tables.Table):
    nombre = tables.Column(verbose_name="Nombre del item")
    my_column = tables.TemplateColumn(verbose_name=('Acciones'),
                                    template_name='columna_item.html',
                                    sortable=False)
    class Meta:
        model = Item
        attrs = {"class": "paleblue"}
        fields = ("nombre", "id", "tipoitem", "complejidad", "costo", "estado", "version", "archivo")
        sequence = ("nombre", "id", "tipoitem", "complejidad", "costo", "estado", "version", "archivo")


class RevivirItemTable(tables.Table):
    nombre = tables.Column(verbose_name="Nombre del item")
    my_column = tables.TemplateColumn(verbose_name=('Acciones'),
                                    template_code='<a href="/item/revivir_item/{{ record.id }}"><input class="btn btn-xs btn-default" type="submit" name="submit" value="Revivir" /></a>',
                                    sortable=False)
    class Meta:
        model = Item
        attrs = {"class": "paleblue"}
        fields = ("nombre", "id","complejidad","costo","estado","version","archivo")
        sequence = ("nombre", "id","complejidad","costo","estado","version","archivo")

class RevertirItemTable(tables.Table):
    nombre = tables.Column(verbose_name="Nombre del item")
    my_column = tables.TemplateColumn(verbose_name=('Acciones'),
                                    template_code='<a href="/item/revertir_item/{{ record.id }}/{{ record.version }}"><input class="btn btn-xs btn-default" type="submit" name="submit" value="Revertir" /></a>',
                                    sortable=False)
    class Meta:
        model = Item
        attrs = {"class": "paleblue"}
        fields = ("nombre", "id","complejidad","costo","estado","version")
        sequence = ("nombre", "id","complejidad","costo","estado","version")