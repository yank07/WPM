from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from proyecto.models import Proyecto
from eav.models import Attribute
__author__ = 'ccaballero'


class TestAdd_tipoitem(TestCase):
    """
    Clase que implementa el test para la vista add_tipoitem
    """

    def setUp(self):
        """
        Metodo de preparacion de test
        """
        #creamos usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        #creamos proyecto
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna',
                                                presupuesto=111, nombre='proyecto_test', estado='Pendiente')
        #obtenemos la 1ra fase del proyecto
        self.fase1 = self.proyecto.fases.first()
        #creamos un atributo
        self.atributo = Attribute.objects.create(name='test', datatype='int',required=False)

    def test_add_tipoitem(self):
        """
        Metodo de test
        """
        c = Client()
        #iniciasr sesion
        c.login(username='super', password='super')
        url = reverse('add_tipoitem')
        #creamos POST
        response = c.post(url, {'nombre': 'tipoitem', 'descripcion': 'test', 'observacion': 'test',
                                    'atributos': self.atributo.id, 'fases': self.fase1.id}, follow=True)
        #el test pasa si la vista redirige a /admin_tipoitem
        self.assertRedirects(response, '/admin_tipoitem/')
