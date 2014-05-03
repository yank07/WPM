from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from proyecto.models import Proyecto

__author__ = 'ccaballero'


class TestAdd_atributo(TestCase):
    """
    Clase de implementacion de test de vista add_atributo
    """

    def setUp(self):
        """
        Metodo de preparacion de test
        """
        #crear usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')

    def test_add_atributo(self):
        """
        Metodo de test
        """
        c = Client()
        #iniciar sesion
        c.login(username='super', password='super')
        #obtener url
        url = reverse('add_atributo')
        #hacemos un POST a la vista
        response = c.post(url, {'nombre_atributo': 'test1', 'tipo': 'int'}, follow=True)
        #el test pasa si la vista redirige a /listar_atributos/
        self.assertRedirects(response, '/listar_atributos/')