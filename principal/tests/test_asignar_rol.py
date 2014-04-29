from unittest import TestCase
from django.contrib.auth.models import User, Group
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
__author__ = 'ccaballero'


class TestAsignar_rol(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.group = Group.objects.create(name='rol_test')

    def test_asignar_rol(self):
        c = Client()
        c.login(username='super', password='super')
        user = User.objects.get(username='super')
        rol = Group.objects.get(name='rol_test')
        response = c.post(reverse('asignar_rol'), {'username': user.id, 'groups': rol.id}, follow=True)
        self.assertRedirects(response, '/admin_roles/')