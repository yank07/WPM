from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from eav.models import Attribute
from TipoItemApp.models import TipoItem
from proyecto.models import Proyecto, Fase

__author__ = 'ccaballero'


class TestDelete_tipoitem(TestCase):
    """
    Clase de test para la vista delete_tipoitem
    """

    def setUp(self):
        """
        Metodo de preparacion de test
        """
        #crear usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        #crear proyecto
        self.p = Proyecto.objects.create(usuario=self.user,nombre='proy1',presupuesto=123,
                                    observaciones='ninguna',estado='Activo',numero_fases=1)
        #obtener fase
        self.fase = Fase.objects.get(proyecto__id=self.p.id)
        #crear atributo
        self.attr1 = Attribute.objects.create(name='att1',datatype='int',required=False)
        #crear tipo item
        self.tipoitem = TipoItem.objects.create(nombre='tipo1',descripcion='desc',observacion='ninguna')
        #asignar atributo a tipo item
        self.tipoitem.atributos.add(self.attr1)
        #asignar tipo item a la fase
        self.tipoitem.fases.add(self.fase)

    def test_delete_tipoitem(self):
        """
        Metodo de test
        """
        c = Client()
        #iniciar sesion
        c.login(username='super', password='super')
        #obtener url con parametro adecuado
        url = reverse('delete_tipoitem', args=[self.tipoitem.id])
        #hacemos POST
        response = c.post(url, follow=True)
        #el test pasa si la vista redirige a /admin_tipoitem
        self.assertRedirects(response, '/admin_tipoitem/')