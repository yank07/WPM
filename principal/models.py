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









