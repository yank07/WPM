from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User
from proyecto.models import Proyecto

__author__ = 'ccaballero'


class TestReporteFases(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.user2 = User.objects.create_user('user2', 'lennon@thebeatles.com', 'user2')
        self.user3 = User.objects.create_user('user3', 'lennon@thebeatles.com', 'user3')
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna',
                                                presupuesto=111, nombre='proyecto_test', estado='Pendiente')
        self.fase = self.proyecto.fases.first()

    def test_reporte_fases(self):
        c = Client()
        c.login(username='super', password='super')
        url = reverse('reportes.views.reporte_fases', args=[self.fase.id])
        response = c.get(url, follow=True)
        self.assertEqual(response.status_code, 200)