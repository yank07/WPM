from unittest import TestCase
from django.contrib.auth.models import User, Group
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
__author__ = 'ccaballero'


class TestDelete_rol(TestCase):
    """
    Clase que implementa test de la vista delete_rol
    """

    def setUp(self):
        """
        Metodo de preparacion de test
        """
        #creamos usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        #creamos un rol
        self.group = Group.objects.create(name='rol_test')

    def test_delete_rol(self):
        """
        Metodo de test para la vista delete_rol
        """
        c = Client()
        #iniciamos sesion
        c.login(username='super', password='super')
        #hacemos un POST con el nombre del rol para su eliminacion
        response = c.post('/roles/delete/rol_test/', follow=True)
        #el test pasa si la vista nos redirecciona a /admin/roles/
        self.assertRedirects(response, '/admin_roles/')