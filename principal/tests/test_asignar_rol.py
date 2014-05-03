from unittest import TestCase
from django.contrib.auth.models import User, Group
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
__author__ = 'ccaballero'


class TestAsignar_rol(TestCase):
    """
    Clase que implementa el test para la vista asignar_rol
    """

    def setUp(self):
        """
        Metodo de preparacion del test
        """
        #creamos un usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        #creamos un grupo
        self.group = Group.objects.create(name='rol_test')

    def test_asignar_rol(self):
        """
        Metodo que implementa test de la vista admin_roles
        """
        c = Client()
        #iniciamos sesion
        c.login(username='super', password='super')
        #obtenemos el usuario creado
        user = User.objects.get(username='super')
        #obtenemos el rol creado
        rol = Group.objects.get(name='rol_test')
        #creamos un POST con los valores de rol y usuario
        response = c.post(reverse('asignar_rol'), {'username': user.id, 'groups': rol.id}, follow=True)
        #la vista funciona cuando nos redirige a /admin_roles/
        self.assertRedirects(response, '/admin_roles/')