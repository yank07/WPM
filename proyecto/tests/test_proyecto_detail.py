from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from proyecto.models import Proyecto

__author__ = 'ccaballero'


class TestProyecto_detail(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna', presupuesto=111, nombre='proyecto_test', estado='Pendiente')

    def test_proyecto_detail(self):
        c = Client()
        c.login(username='super', password='super')
        p = Proyecto.objects.get(nombre='proyecto_test')
        url = reverse('proyecto_detail', args=[p.id])
        response = c.post(url, {'miembros':self.user.id, 'numero_fases':2, 'usuario':self.user.id, 'observaciones':'asdf', 'presupuesto':111, 'nombre':'proyecto_test', 'estado':'Pendiente'}, follow=True)
        self.assertRedirects(response, '/admin_proyectos/')