import django_tables2 as tables
from TipoItemApp.models import TipoItem
from proyecto.models import Proyecto, Fase
from django_tables2.utils import A
from eav.models import Attribute




class TipoItemTable(tables.Table):
    nombre = tables.Column(verbose_name="Nombre del Tipo de Item")
    my_column = tables.TemplateColumn(verbose_name=('Acciones'),
                                    template_code='<a href="/edit_tipoitem/{{ record.id }}"><input class="btn btn-xs btn-default" type="submit" name="submit" value="Editar" /></a>',
                                    sortable=False)
    class Meta:
        model = TipoItem
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
        fields = ("nombre", "observacion" , "descripcion")
        sequence = ("nombre", "observacion" , "descripcion")


class AtributoTable(tables.Table):
    #nombre = tables.Column(verbose_name="Nombre del Atributo")
    my_column = tables.TemplateColumn(verbose_name=('Acciones'),
                                    template_code='<a href="/edit_atributo/{{ record.id }}"><input class="btn btn-xs btn-default" type="submit" name="submit" value="Editar" /></a>',
                                    sortable=False)
    class Meta:
        model = Attribute
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
        fields = ("name", "datatype", "required")
        sequence = ("name", "datatype" , "required")