from unittest import TestCase
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

__author__ = 'ccaballero'


class TestAdmin_usuario(TestCase):
    """
    Clase que implementa el test para vista admin_usuario
    """

    def setUp(self):
        """
        Metodo de preparacion de test
        """
        self.client = Client()
        #creamos un usuario en la db
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')

    def test_admin_usuario(self):
        """
        Metodo de test de vista admin_usuario
        """
        c = Client()
        #iniciar sesion
        c.login(username='super', password='super')
        #hacemos una peticion GET a la vista
        response = c.get(reverse('admin_usuario'))
        #la vista funciona si el codigo de respuesta es 200
        self.assertEqual(response.status_code, 200)