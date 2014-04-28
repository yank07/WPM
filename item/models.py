from django.db import models
from TipoItemApp.models import TipoItem
from proyecto.models import Fase


class Item(models.Model):
    ESTADOS_CHOICES = (
        ('ACT','Activo'),
        ('REV','Revision'),
        ('APROB','Aprobado'),
        ('BLOQ','Bloqueado'),
        ('ELIM','Eliminado')
    )
    nombre = models.CharField(max_length=50, help_text='Nombre del Item',unique=False)
    tipoitem=models.ForeignKey(TipoItem,unique=False,related_name='tipoitem',help_text='Tipo de Item FK')
    fase=models.ForeignKey(Fase,unique=False,related_name='fase',help_text='Fase asociado al Item')
    complejidad= models.IntegerField(help_text='Complejidad del item. [1-100]')
    costo= models.IntegerField(help_text='Costo monerario del item')
    estado=models.CharField(max_length=5,choices=ESTADOS_CHOICES,default='ACT')
    descripcion = models.CharField(max_length=50, help_text='Descripcion del Item')
    observacion = models.CharField(blank=True,max_length=50, help_text='Observacion del Item')
    id_item=models.IntegerField(blank=True, null=True,help_text='Diferentes versiones de un item tienen el mismo id_item')
    version=models.IntegerField(blank=True,default=0,help_text='Version del Item')
    fecha_creacion=models.DateField(auto_now_add=True)
    fecha_modificacion=models.DateField(auto_now=True)
    archivo=models.FileField(blank=True,upload_to='files')

    #estuvo en linea base?
    def __unicode__(self):
        return unicode(self.nombre)

class relaciones(models.Model):
    RELACION_CHOICES = (
        ('HIJ','Padre-Hijo'),
        ('SUC','Antecesor-Sucesor'),
    )
    tipo_relacion=models.CharField(max_length=3,choices=RELACION_CHOICES,default='HIJ',help_text='Tipo de relacion')
    item_origen=models.ForeignKey(Item,related_name='item_origen',help_text='Item Origen de la relacion')
    item_destino=models.ForeignKey(Item,related_name='item_destino',help_text='Item Destino de la relacion')
    class Meta:
        unique_together=('item_origen','item_destino')
    #unique(origen+destino)