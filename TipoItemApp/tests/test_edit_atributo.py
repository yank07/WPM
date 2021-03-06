from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from eav.models import Attribute

__author__ = 'ccaballero'


class TestEdit_atributo(TestCase):
    """
    Clase de test para vista edit_atributo
    """

    def setUp(self):
        """
        Metodo de preparacion
        """
        #crear usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        #crear atibuto
        self.atributo = Attribute.objects.create(name='test', datatype='int',required=False)

    def test_edit_atributo(self):
        """
        Metodo de test
        """
        c = Client()
        #iniciar sesion
        c.login(username='super', password='super')
        #obtener url con parametros adecuados
        url = reverse('edit_atributo',args=[self.atributo.id])
        #hacemos POST
        response = c.post(url, {'nombre': 'test1', 'tipo': 'int'}, follow=True)
        #el test pasa si la vista redirige a /listar_atributos
        self.assertRedirects(response, '/listar_atributos/')