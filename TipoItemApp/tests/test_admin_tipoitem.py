from unittest import TestCase
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

__author__ = 'ccaballero'


class TestAdmin_tipoitem(TestCase):
    """
    Clase de test para la vista admin_tipoitem
    """

    def setUp(self):
        """
        Metodo de preparacion de test
        """
        #crear usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')

    def test_admin_tipoitem(self):
        """
        Metodo de test
        """
        c = Client()
        #iniciar sesion
        c.login(username='super', password='super')
        url = reverse('admin_tipoitem')
        #hacemos un GET
        response = c.get(url)
        #el test pasa si el codigo de respuesta es 200
        self.assertEqual(response.status_code, 200)