from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from eav.models import Attribute

__author__ = 'ccaballero'


class TestDelete_atributo(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.atributo = Attribute.objects.create(name='test', datatype='int',required=False)

    def test_delete_atributo(self):
        c = Client()
        c.login(username='super', password='super')
        url = reverse('delete_atributo', args=[self.atributo.id])
        response = c.post(url, follow=True)
        self.assertRedirects(response, '/listar_atributos/')