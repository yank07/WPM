from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from proyecto.models import Proyecto
from eav.models import Attribute
__author__ = 'ccaballero'


class TestAdd_tipoitem(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna',
                                                presupuesto=111, nombre='proyecto_test', estado='Pendiente')
        self.fase1 = self.proyecto.fases.first()
        self.atributo = Attribute.objects.create(name='test', datatype='int',required=False)

    def test_add_tipoitem(self):
            c = Client()
            c.login(username='super', password='super')
            url = reverse('add_tipoitem')
            response = c.post(url, {'nombre': 'tipoitem', 'descripcion': 'test', 'observacion': 'test',
                                    'atributos': self.atributo.id, 'fases': self.fase1.id}, follow=True)
            self.assertRedirects(response, '/admin_tipoitem/')
