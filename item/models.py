from django.db import models
from simple_history.models import HistoricalRecords
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
    tipoitem=models.ForeignKey(TipoItem,unique=False,related_name='item',help_text='Tipo de Item FK')
    fase=models.ForeignKey(Fase,unique=False,related_name='item',help_text='Fase asociado al Item')
    complejidad= models.IntegerField(help_text='Complejidad del item. [1-100]')
    costo= models.IntegerField(help_text='Costo monerario del item')
    estado=models.CharField(max_length=5,choices=ESTADOS_CHOICES,default='ACT')
    descripcion = models.CharField(max_length=50, help_text='Descripcion del Item')
    observacion = models.CharField(blank=True,max_length=50, help_text='Observacion del Item')
    #id_item=models.IntegerField(blank=True, null=True,help_text='Diferentes versiones de un item tienen el mismo id_item')
    version=models.IntegerField(default=0,help_text='Version del Item')
    fecha_creacion=models.DateField(auto_now_add=True)
    fecha_modificacion=models.DateField(auto_now=True)
    archivo=models.FileField(blank=True,upload_to='files')
    history = HistoricalRecords()
    rango_valor_inicio = models.IntegerField(default=0,help_text='Inicio de los valores para los atributos')
    rango_valor_final = models.IntegerField(default=0,help_text='Final de los valores para los atributos')
    #estuvo en linea base?
    class Meta:
        unique_together=('nombre','version')
    def __unicode__(self):
        return unicode(self.nombre)
    def cambiar_estado(self,estado):
        self.estado=estado
        self.save()
        self.history.last().delete()
    def copy(self,item):
        self.id=item.id
        self.nombre=item.nombre
        self.tipoitem_id=item.tipoitem_id
        self.fase_id=item.fase_id
        self.complejidad=item.complejidad
        self.costo=item.costo
        self.estado=item.estado
        self.descripcion=item.descripcion
        self.observacion=item.observacion
        self.version=item.version
        self.fecha_creacion=item.fecha_creacion
        self.fecha_modificacion=item.fecha_modificacion
        self.archivo=item.archivo
        self.rango_valor_inicio = item.rango_valor_inicio
        self.rango_valor_final = item.rango_valor_final

class relaciones(models.Model):
    RELACION_CHOICES = (
        ('HIJ','Padre-Hijo'),
        ('SUC','Antecesor-Sucesor'),
    )
    tipo_relacion=models.CharField(max_length=3,choices=RELACION_CHOICES,default='HIJ',help_text='Tipo de relacion')
    item_origen=models.ForeignKey(Item,related_name='item_origen',help_text='Item Origen de la relacion')
    item_destino=models.ForeignKey(Item,related_name='item_destino',help_text='Item Destino de la relacion')
    activo = models.BooleanField(default=True, help_text='Si activo=True significa que el item no esta eliminado')
    item_origen_version=models.IntegerField(default=0,help_text='Version del Item Origen')
    item_destino_version=models.IntegerField(default=0,help_text='Version del Item Destino')
    class Meta:
        unique_together=('item_origen','item_destino')