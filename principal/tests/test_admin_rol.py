from unittest import TestCase
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
__author__ = 'ccaballero'


class TestAdmin_rol(TestCase):
    """
    Clase que implementa test para la vista admin_rol
    """

    def setUp(self):
        """
        Metodo de preparacion del test
        """
        self.client = Client()
        #creamos un usuario en la bd de prueba
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')

    def test_admin_rol(self):
        """
        Metodo de test de vista admin_rol
        """
        c = Client()
        #iniciamos sesion
        c.login(username='super', password='super')
        #hacemos una peticion GET a la vista
        response = c.get(reverse('admin_rol'))
        #la vista funciona si la respuesta HTTP es 200
        self.assertEqual(response.status_code, 200)