__author__ = 'ccaballero'
from unittest import TestCase
from django.contrib.auth.models import User, Group
from django.test import Client, TestCase
from django.core.urlresolvers import reverse


class TestEdit_rol(TestCase):
    """
    Clase que implementa el test para la vista edit_rol
    """

    def setUp(self):
        """
        Metodo de preparacion del test
        """

        self.client = Client()
        #creamos usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        #creamos grupo
        self.group = Group.objects.create(name='rol_test')

    def test_edit_rol(self):
        """
        Metodo que implementa el test de la vista edit_rol
        """
        c = Client()
        #iniciamos sesion
        c.login(username='super', password='super')
        #creamos un POST con los datos nuevos para el grupo
        response = c.post(reverse('edit_rol', args=['rol_test']), {'name': 'rol_test', 'permissions': 8}, follow=True)
        #el test pasa si la vista nos redirige a /admin/roles/
        self.assertRedirects(response, '/admin_roles/')