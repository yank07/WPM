from django.db import models
from django.contrib.auth.models import User

# Create your models here.



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



