from django.db import models
from django.contrib.auth.models import User
from item.models import Item
# Create your models here.


class Solicitud(models.Model):
    """
    Modelo para la solicitud de cambio
    """
    usuario = models.ForeignKey(User, related_name='solicitud_cambio', help_text='Usuario creador de la SC')
    item = models.ForeignKey(Item, related_name='solicitud_cambio', help_text='Item solicitado')
    fecha_caducar = models.DateField(max_length=200, help_text='Observaciones del proyecto')
    motivo = models.TextField(max_length=200, help_text='Motivo de la solicitud')
    impacto = models.IntegerField(default=0, help_text='Resultado del calculo de impacto')
    votos = models.IntegerField(default=0, help_text='Votos del comite')

    class Meta:
        permissions = (('crear_solicitud', 'crear_solicitud'))

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
    primer_integrante = models.ForeignKey(User, blank=True, related_name='comite', help_text='Primer integrante')
    segundo_integrante = models.ForeignKey(User, blank=True, related_name='comite', help_text='Segundo integrante')
    tercer_integrante = models.ForeignKey(User, blank=True, related_name='comite', help_text='Tercero integrante')
    estado = models.CharField(max_length=3, choices=ESTADOS_CHOICES)

    def __unicode__(self):
        return unicode('Comite '+str(self.id))