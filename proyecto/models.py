from django.db import models
from django.contrib.auth.models import User, Permission
from django.db.models import signals

# Create your models here.

ESTADO_CHOICES=(
('Pendiente', 'Pendiente'),
('Activo', 'Activo'),
('Cancelado', 'Cancelado'),
('Finalizado','Finalizado'),
)


def crear_fases(sender, instance, created, **kwargs):
    print "Post save emited for", instance.numero_fases
    for x in range(0, instance.numero_fases):
        p = Fase(nombre='fase'+ str(x+1), proyecto=instance)
        p.save()

class Proyecto(models.Model):
    """
    Guarda una entrada de un proyecto.

    """
    usuario = models.ForeignKey(User,related_name='proyectos', help_text='Usuario creador del proyecto')
    nombre=models.CharField(max_length=50, help_text='Nombre del Proyecto')
    presupuesto=models.IntegerField(default=0, help_text='Presupuesto del proyecto')
    observaciones=models.TextField(max_length=200, help_text='Observaciones del proyecto')
    estado = models.CharField(max_length=50, help_text='Descriocion del Estado del Proyecto', choices=ESTADO_CHOICES)
    numero_fases=models.IntegerField(default=1, help_text='Presupuesto del proyecto')


    def __unicode__(self):
        """
        Devuelve el nombre del proyecto
        @return el nombre del proyecto
        """
        return unicode(self.nombre)

signals.post_save.connect(crear_fases, sender=Proyecto)

class Fase(models.Model):
    """
    Modelo que maneja las fases de un proyecto
    """
    proyecto = models.ForeignKey(Proyecto,related_name='fases', help_text='Proyecto al que pertenece la fase')
    nombre=models.CharField(max_length=50, help_text='Nombre de la fase')

    def __unicode__(self):
        return unicode(self.nombre)