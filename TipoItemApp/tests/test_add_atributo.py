from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from proyecto.models import Proyecto

__author__ = 'ccaballero'


class TestAdd_atributo(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        # self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna', presupuesto=111, nombre='proyecto_test', estado='Pendiente')
        # self.fase1 = self.proyecto.fases.first()
        # self.fase2 = self.proyecto.fases.last()

    def test_add_atributo(self):
        c = Client()
        c.login(username='super', password='super')
        url = reverse('add_atributo')
        response = c.post(url, {'nombre_atributo': 'test1', 'tipo': 'int'}, follow=True)
        self.assertRedirects(response, '/listar_atributos/')