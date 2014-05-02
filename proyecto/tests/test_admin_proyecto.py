from unittest import TestCase
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

__author__ = 'ccaballero'


class TestAdmin_proyecto(TestCase):
    """
    Clase que implementa el test para la vista admin_proyecto
    """

    def setUp(self):
        """
        Metodo de preparacion del test
        """
        #creamos un usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')

    def test_admin_proyecto(self):
        """
        Metodo que implementa el test de la vista admin_proyecto
        """
        c = Client()
        #iniciamos sesion
        c.login(username='super', password='super')
        #hacemos un GET a la vista
        response = c.get('/admin_proyectos/', follow=True)
        #el test pasa si el codigo HTTP de respuesta es 200
        self.assertEqual(response.status_code, 200)