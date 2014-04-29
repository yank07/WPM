from unittest import TestCase
from django.contrib.auth.models import User, Group
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
__author__ = 'ccaballero'


class TestDelete_rol(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.group = Group.objects.create(name='rol_test')

    def test_delete_rol(self):
        c = Client()
        c.login(username='super', password='super')
        response = c.post('/roles/delete/rol_test/', follow=True)
        #response = c.post(reverse('delete_rol', args=['rol_test']), follow=True)
        #response = c.post(reverse('delete_rol', args=['rol_test']), follow=True)
        self.assertRedirects(response, '/admin_roles/')