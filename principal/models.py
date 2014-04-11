"""
Creado el 1 abril 2014
@author: Grupo 04
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

## el modelo de usuarios de django ya contempla nombre de usuario, direccion
## de correo y contrasenha


class UserProfile(models.Model):

    user = models.ForeignKey(User, unique=True)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=15)
    activo=models.BooleanField(default=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
#
# class UserProfile(models.Model):
#     user = models.ForeignKey(User, unique=True)
#     direccion=models.CharField(max_length=50)
#     telefono=models.CharField(max_length=15)
#
# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class EstadosProyecto(models.Model):
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.descripcion)


class Proyecto(models.Model):
    """
    Guarda una entrada de un proyecto, related to `auth.User`

    """
    usuario = models.ForeignKey(User,related_name='proyectos' )
    nombre=models.CharField(max_length=50)
    presupuesto=models.IntegerField(default=0)
    observaciones=models.TextField(max_length=200)
    estado = models.ForeignKey(EstadosProyecto, blank=True, null=True)


    def __unicode__(self):
        return unicode(self.nombre)

class Fase(models.Model):
    """
    Modelo que maneja las fases de un proyecto
    """
    proyecto = models.ForeignKey(User,related_name='fases' )
    nombre=models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.nombre)



