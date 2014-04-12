"""
Creado el 1 abril 2014
@author: Grupo 04
"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Permission

# Create your models here.

## el modelo de usuarios de django ya contempla nombre de usuario, direccion
## de correo y contrasenha

# class Rol(models.Model):
#     """
#     Modelo para el tratamiento de los roles
#     """
#     permisos = models.ManyToManyField(Permission)
#     #usuarios = models.ManyToManyField(User)
#     nombre=models.CharField(max_length=50,unique=True) #debe ser unico
#     #descripcion = models.TextField(max_length=200, default='')
#     def __unicode__(self):
#         return unicode(self.nombre)


class UserProfile(models.Model):
    """
    Guarda un perfil de usuario. Como el modelo de usuarios de django ya almacena nombre,
    password y direccion de email, se extiende la funcionalidad para almacenar direccion,
    telefono y estado.
    """
    user = models.ForeignKey(User, unique=True, help_text='Usuario al que pertenece el perfil')
    direccion=models.CharField(max_length=50, help_text='Direccion del usuario')
    telefono=models.CharField(max_length=15, help_text='Telefono del usuario')
    activo=models.BooleanField(default=True, help_text='Estado del usuario')
    #roles=models.ManyToManyField(Rol, help_text='Roles de usuario')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class EstadosProyecto(models.Model):
    """
    Guarda los estados posibles de un proyecto.
    """
    descripcion = models.CharField(max_length=50, help_text='Descriocion del Estado del Proyecto')

    def __unicode__(self):
        """
        Retorna la descripcion del estado
        @return la descripcion del estado
        """
        return unicode(self.descripcion)


class Proyecto(models.Model):
    """
    Guarda una entrada de un proyecto.

    """
    usuario = models.ForeignKey(User,related_name='proyectos', help_text='Usuario creador del proyecto')
    nombre=models.CharField(max_length=50, help_text='Nombre del Proyecto')
    presupuesto=models.IntegerField(default=0, help_text='Presupuesto del proyecto')
    observaciones=models.TextField(max_length=200, help_text='Observaciones del proyecto')
    estado = models.ForeignKey(EstadosProyecto, blank=True, null=True, help_text='Estado del proyecto')


    def __unicode__(self):
        """
        Devuelve el nombre del proyecto
        @return el nombre del proyecto
        """
        return unicode(self.nombre)

class Fase(models.Model):
    """
    Modelo que maneja las fases de un proyecto
    """
    proyecto = models.ForeignKey(User,related_name='fases', help_text='Proyecto al que pertenece la fase')
    nombre=models.CharField(max_length=50, help_text='Nombre de la fase')

    def __unicode__(self):
        return unicode(self.nombre)




