from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User
from proyecto.models import Proyecto
from solicitudCambio.models import Comite

__author__ = 'ccaballero'


class TestReporteResumenProyecto(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.user2 = User.objects.create_user('user2', 'lennon@thebeatles.com', 'user2')
        self.user3 = User.objects.create_user('user3', 'lennon@thebeatles.com', 'user3')
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna',
                                                presupuesto=111, nombre='proyecto_test', estado='Pendiente')
        self.comite = Comite.objects.create(proyecto=self.proyecto, primer_integrante=self.user,
                                            segundo_integrante=self.user2, tercer_integrante=self.user3, estado='ACT')

    def test_reporte_resumen_proyecto(self):
        c = Client()
        c.login(username='super', password='super')
        url = reverse('reportes.views.reporte_resumen_proyecto', args=[self.proyecto.id])
        response = c.get(url, follow=True)
        self.assertEqual(response.status_code, 200)