from unittest import TestCase
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

__author__ = 'ccaballero'


class TestAdmin_proyecto(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')

    def test_admin_proyecto(self):
        c = Client()
        c.login(username='super', password='super')
        response = c.get('/admin_proyectos/', follow=True)
        self.assertEqual(response.status_code, 200)