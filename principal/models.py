from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=15)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Proyecto(models.Model):
    usuario = models.ForeignKey(User,related_name='proyectos' )
    nombre=models.CharField(max_length=50)



    def __unicode__(self):
        return unicode(self.nombre)


class Fase(models.Model):
    proyecto = models.ForeignKey(User,related_name='fases' )
    nombre=models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.nombre)



