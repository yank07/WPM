#from unittest import TestCase
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

__author__ = 'ccaballero'


class TestAdd_rol(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')


    def test_add_rol(self):
        c = Client()
        c.login(username='super', password='super')
        respuesta_guardado = c.post(reverse('add_rol'), {'name': 'rol_test', 'permissions': 8}, follow=True)
        self.assertRedirects(respuesta_guardado, '/admin_roles/')