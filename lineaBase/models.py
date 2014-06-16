from django.db import models
from item.models import Item
from proyecto.models import Fase

# Create your models here.


class LineaBase(models.Model):
    """
    Modelo de la Linea Base
    """
    ESTADOS_CHOICES = (
        ('ABIERTA','Abierta'),
        ('CERRADA','Cerrada'),

    )
    descripcion = models.CharField(max_length=50, help_text='Descripcion de la Linea Base',unique=False)
    estado = models.CharField(max_length=20,choices=ESTADOS_CHOICES,default='CERRADA')
    items = models.ManyToManyField(Item,related_name='linea_base',help_text='Item dentro de la linea base')
    fase = models.ForeignKey(Fase,related_name='linea_base',help_text='Fase a la que pertenece la linea Base',blank=True,null=True)


