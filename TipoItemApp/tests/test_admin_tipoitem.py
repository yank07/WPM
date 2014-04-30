from unittest import TestCase
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

__author__ = 'ccaballero'


class TestAdmin_tipoitem(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')

    def test_admin_tipoitem(self):
        c = Client()
        c.login(username='super', password='super')
        url = reverse('admin_tipoitem')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)