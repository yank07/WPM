#from unittest import TestCase
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

__author__ = 'ccaballero'


class TestAdd_rol(TestCase):
    """
    Clase de test unitario de la vista add_rol
    """

    def setUp(self):
        """
        Metodo que se ejecuta antes del test
        """
        #creamos un cliente http
        self.client = Client()
        #creamos un usuario en la base de datos de prueba
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')


    def test_add_rol(self):
        """
        El test de la vista add_rol
        """
        c = Client()
        #iniciamos sesion con el usuario creado previamente
        c.login(username='super', password='super')
        #hacemos una peticion POST para la vista
        respuesta_guardado = c.post(reverse('add_rol'), {'name': 'rol_test', 'permissions': 8}, follow=True)
        #como sabemos que la vista funciona? cuando nos redirecciona a admin_roles
        self.assertRedirects(respuesta_guardado, '/admin_roles/')