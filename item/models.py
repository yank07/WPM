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
    nombre = models.CharField(max_length=50, help_text='Nombre del Item')
    tipoitem=models.ForeignKey(TipoItem,unique=False,related_name='item',help_text='Tipo de Item FK')
    fase=models.ForeignKey(Fase,unique=False,related_name='item',help_text='Fase asociado al Item')
    complejidad= models.IntegerField(help_text='Complejidad del item. [1-100]')
    costo= models.IntegerField(help_text='Costo monerario del item')
    estado=models.CharField(max_length=5,choices=ESTADOS_CHOICES,default='ACT')
    descripcion = models.CharField(max_length=50, help_text='Descripcion del Item')
    observacion = models.CharField(blank=True,max_length=50, help_text='Observacion del Item')
    fecha_creacion=models.DateField(auto_now_add=True)
    fecha_modificacion=models.DateField(auto_now=True)
    archivo=models.FileField(blank=True,upload_to='ninguno/')
    #relaciones
    def __unicode__(self):
        return unicode(self.nombre)
