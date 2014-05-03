from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

__author__ = 'ccaballero'


class TestAdd_proyecto(TestCase):
    """
    Clase que implementa el test para vista add_proyecto
    """

    def setUp(self):
        """
        Metodo de preparacion del test
        """
        #creamos usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')

    def test_add_proyecto(self):
        """
        Metodo que implementa el test para la vista add_proyecto
        """
        c = Client()
        #iniciamos sesion
        c.login(username='super', password='super')
        #hacemos un POST a la vista
        response = c.post('/add_proyecto/', {'miembros': self.user.id, 'numero_fases': 2, 'usuario': self.user.id, 'observaciones': 'ninguna', 'presupuesto': 1111, 'nombre': 'test1', 'estado': 'Pendiente'}, follow=True)
        #el test pasa si la vista nos redirige a /admin/proyectos
        self.assertRedirects(response, '/admin_proyectos/')