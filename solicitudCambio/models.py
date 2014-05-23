from django.db import models
from django.contrib.auth.models import User
from item.models import Item
from proyecto.models import Proyecto


class Solicitud(models.Model):
    """
    Modelo para la solicitud de cambio
    """
    ESTADOS_CHOICES = (
        ('PEN', 'Pendiente'),
        ('APR', 'Aprobada'),
        ('DEN', 'Denegada')
    )

    usuario = models.ForeignKey(User, related_name='solicitud_cambio', help_text='Usuario creador de la SC')
    item = models.ForeignKey(Item, related_name='solicitud_cambio', help_text='Item solicitado')
    fecha_caducar = models.DateField(max_length=200, help_text='fecha')
    motivo = models.TextField(max_length=200, help_text='Motivo de la solicitud')
    impacto = models.IntegerField(default=0, help_text='Resultado del calculo de impacto')

    voto_primero = models.IntegerField(default=0, help_text='Voto del primer integrante')
    voto_segundo = models.IntegerField(default=0, help_text='Voto del segundo integrante')
    voto_tercero = models.IntegerField(default=0, help_text='Voto del tercer integrante')
    conteo = models.IntegerField(default=0, help_text='Conteo')
    resultado = models.IntegerField(default=0, help_text='Resultado')
    estado = models.CharField(max_length=3, choices=ESTADOS_CHOICES, help_text='Estados')

    def __unicode__(self):
        return unicode('Solicitud '+str(self.id))


class Comite(models.Model):
    """
    Modelo para los miembros del comite
    """
    ESTADOS_CHOICES = (
        ('ACT','Activo'),
        ('INA','Inactivo'),
    )
    proyecto = models.ForeignKey(Proyecto, related_name='proyecto', help_text='Proyecto del comite')
    primer_integrante = models.ForeignKey(User, blank=True, related_name='primero', help_text='Primer integrante')
    segundo_integrante = models.ForeignKey(User, blank=True, related_name='segundo', help_text='Segundo integrante')
    tercer_integrante = models.ForeignKey(User, blank=True, related_name='tercero', help_text='Tercero integrante')
    estado = models.CharField(max_length=3, choices=ESTADOS_CHOICES)

    def __unicode__(self):
        return unicode('Comite '+str(self.id))