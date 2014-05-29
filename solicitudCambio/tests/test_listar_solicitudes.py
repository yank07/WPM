from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User
from proyecto.models import Proyecto

__author__ = 'ccaballero'


class TestListarSolicitudes(TestCase):
    """
    Clase de test para la vista solicitudCambio.views.listar_solicitudes
    """

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna',
                                                presupuesto=111, nombre='proyecto_test', estado='Pendiente')
        self.fase = self.proyecto.fases.first()

    def test_listar_solicitudes(self):
        c = Client()
        c.login(username='super', password='super')
        url = reverse('solicitudCambio.views.listar_solicitudes')
        response = c.get(url, follow=True)
        self.assertEqual(response.status_code, 200)