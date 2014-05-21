from django.contrib.auth.models import User
from django.test import Client, TestCase
from proyecto.models import Proyecto, Fase
from django.core.urlresolvers import reverse

__author__ = 'ccaballero'


class TestAdmin_lb(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna',
                                                presupuesto=111, nombre='proyecto_test', estado='Pendiente')
        self.fase = self.proyecto.fases.first()

    def test_admin_lb(self):
        c = Client()
        c.login(username='super', password='super')
        url = reverse('lineaBase.views.admin_lb', args=[self.fase.id])
        response = c.get(url)
        self.assertEqual(response.status_code, 200)