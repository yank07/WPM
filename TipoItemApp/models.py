from django.db import models
from eav.models import Attribute, Value
from eav.registry import EavConfig
from south.modelsinspector import add_ignored_fields
from proyecto.models import Fase

class TipoItem(models.Model):
    """
    Modelo que maneja los tipos de item con sus atributos
    """
    nombre = models.CharField(max_length=50,unique=True, help_text='Nombre del Tipo de Item')
    descripcion = models.CharField(max_length=50, help_text='Descripcion del Tipo de Item')
    observacion = models.CharField(null=True,max_length=50, help_text='Observacion del Tipo de Item')
    atributos = models.ManyToManyField(Attribute,related_name='tipoitem', help_text='Atributos del tipo de item',null=True)
    fases = models.ManyToManyField(Fase,related_name='tipoitem', help_text='Fases asociadas al tipo de item',null=True)
    fecha_creacion = models.DateField(auto_now_add=True, help_text="Fecha de creacion")
    fecha_modificacion = models.DateField(auto_now=True, help_text="Fecha de ultima modificacion")

    def __unicode__(self):
        return unicode(self.nombre)


add_ignored_fields(["^eav\.fields\.EavDatatypeField"])
add_ignored_fields(["^eav\.fields\.EavSlugField"])

# class TipoItemEavConfig(EavConfig):
#     @classmethod
#     def get_attributes(cls):
#         return Attribute.objects.filter(type='tipoitem')

#eav.register(TipoItem, TipoItemEavConfig)
