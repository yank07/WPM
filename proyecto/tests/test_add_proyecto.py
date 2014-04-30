from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

__author__ = 'ccaballero'


class TestAdd_proyecto(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')

    def test_add_proyecto(self):
        c = Client()
        c.login(username='super', password='super')
        response = c.post('/add_proyecto/', {'miembros': self.user.id, 'numero_fases': 2, 'usuario': self.user.id, 'observaciones': 'ninguna', 'presupuesto': 1111, 'nombre': 'test1', 'estado': 'Pendiente'}, follow=True)
        self.assertRedirects(response, '/admin_proyectos/')