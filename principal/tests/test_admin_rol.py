from unittest import TestCase
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
__author__ = 'ccaballero'


class TestAdmin_rol(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')

    def test_admin_rol(self):
        c = Client()
        c.login(username='super', password='super')
        response = c.get(reverse('admin_rol'))
        self.assertEqual(response.status_code, 200)