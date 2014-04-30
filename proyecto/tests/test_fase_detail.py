from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from proyecto.models import Proyecto, Fase

__author__ = 'ccaballero'


class TestFase_detail(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna', presupuesto=111, nombre='proyecto_test', estado='Pendiente')


    def test_fase_detail(self):
        c = Client()
        c.login(username='super', password='super')
        fase = self.proyecto.fases.first()
        url = reverse('fase_detail', args=[fase.id])
        response = c.post(url, {'nombre': 'fase_prueba', 'proyecto': self.proyecto.id}, follow=True)
        return_url = '/proyecto_view/' + str(self.proyecto.id) + '/'
        self.assertRedirects(response, return_url)