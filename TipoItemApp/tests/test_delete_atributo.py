from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from eav.models import Attribute

__author__ = 'ccaballero'


class TestDelete_atributo(TestCase):
    """
    Clase de test para la vista delete_atributo
    """

    def setUp(self):
        """
        Metodo de preparacion
        """
        #crear usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        #creamos atributo
        self.atributo = Attribute.objects.create(name='test', datatype='int',required=False)

    def test_delete_atributo(self):
        """
        Metodo de test
        """
        c = Client()
        #iniciar sesion
        c.login(username='super', password='super')
        #obtenemos la url y le pasamos como parametro el id del atributo a eliminar
        url = reverse('delete_atributo', args=[self.atributo.id])
        #hacemos un POST
        response = c.post(url, follow=True)
        #el test funciona si la vista redirige a /listar_atributos/
        self.assertRedirects(response, '/listar_atributos/')