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
    """
    Crea Automaticamente las fases del Proyecto
    """

    proyecto_fases_nuevo =  instance.numero_fases
    proyecto_fases_creado = Fase.objects.filter(proyecto__id=instance.id).count()
    print "Numero Nuevo " + str(instance.numero_fases)
    print "Numero anterior " + str(Fase.objects.filter(proyecto__id=instance.id).count())

    if proyecto_fases_nuevo > proyecto_fases_creado:
        for x in range(proyecto_fases_creado, proyecto_fases_nuevo):
            p = Fase(nombre='fase'+ str(x+1), proyecto=instance)
            p.save()
    elif proyecto_fases_nuevo < proyecto_fases_creado:
        for x in range( proyecto_fases_nuevo ,proyecto_fases_creado-1):
            f= Fase.objects.filter(proyecto__id=instance.id).last()
            f.delete()

class Proyecto(models.Model):
    """
    Guarda una entrada de un proyecto.

    """
    usuario = models.ForeignKey(User,related_name='proyectos', help_text='Usuario creador del proyecto')
    nombre=models.CharField(max_length=50, help_text='Nombre del Proyecto')
    presupuesto=models.IntegerField(default=0, help_text='Presupuesto del proyecto')
    observaciones=models.TextField(max_length=200, help_text='Observaciones del proyecto')
    estado = models.CharField(max_length=50, help_text='Descripcion del Estado del Proyecto', choices=ESTADO_CHOICES, default='Pendiente')
    numero_fases=models.IntegerField(default=1, help_text='Presupuesto del proyecto')
    miembros = models.ManyToManyField(User, related_name='miembros', help_text='Miembros del proyecto')
    fecha_creacion = models.DateField(auto_now_add=True, help_text="Fecha de Creacion")
    fecha_modificacion = models.DateField(auto_now=True, help_text="Fecha de Ultima Modificacion")
    usuario_modificacion = models.ForeignKey(User, help_text="Usuario que realizo la ultima modificacion")


    def __unicode__(self):
        """
        Devuelve el nombre del proyecto
        @return el nombre del proyecto
        """
        return unicode(self.nombre)
    def proyecto_detail(self):
        return 'Edit'

signals.post_save.connect(crear_fases, sender=Proyecto)

class Fase(models.Model):
    """
    Modelo que maneja las fases de un proyecto
    """
    proyecto = models.ForeignKey(Proyecto,related_name='fases', help_text='Proyecto al que pertenece la fase')
    nombre=models.CharField(max_length=50, help_text='Nombre de la fase')
    fecha_creacion = models.DateField(auto_now_add=True, help_text="Fecha de Creacion")
    fecha_modificacion = models.DateField(auto_now=True, help_text="Fecha de Ultima Modificacion")
    usuario_modificacion = models.ForeignKey(User, help_text="Usuario que realizo la ultima modificacion")

    def __unicode__(self):
        return unicode(self.proyecto.nombre + '_' + self.nombre)