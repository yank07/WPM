__author__ = 'ccaballero'
from unittest import TestCase
from django.contrib.auth.models import User, Group
from django.test import Client, TestCase
from django.core.urlresolvers import reverse


class TestEdit_rol(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.group = Group.objects.create(name='rol_test')

    def test_edit_rol(self):
        c = Client()
        c.login(username='super', password='super')
        response = c.post(reverse('edit_rol', args=['rol_test']), {'name': 'rol_test', 'permissions': 8}, follow=True)
        self.assertRedirects(response, '/admin_roles/')