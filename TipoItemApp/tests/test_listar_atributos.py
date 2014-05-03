from unittest import TestCase
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
__author__ = 'ccaballero'


class TestListar_atributos(TestCase):
    """
    Clase de test para la vista listar_atributos
    """

    def setUp(self):
        """
        Metodo de preparacion
        """
        #crear usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')

    def test_listar_atributos(self):
        """
        Metodo de test
        """
        c = Client()
        #iniciar sesion
        c.login(username='super', password='super')
        url = reverse('listar_atributos')
        response = c.get(url)
        #el test pasa si la vista responde con codigo 200
        self.assertEqual(response.status_code, 200)