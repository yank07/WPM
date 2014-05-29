from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User
from eav.models import Attribute
from TipoItemApp.models import TipoItem
from item.models import Item
from proyecto.models import Proyecto
from solicitudCambio.models import Solicitud, Comite

__author__ = 'ccaballero'


class TestCrear_comite(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.user2 = User.objects.create_user('user2', 'lennon@thebeatles.com', 'user2')
        self.user3 = User.objects.create_user('user3', 'lennon@thebeatles.com', 'user3')
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna',
                                                presupuesto=111, nombre='proyecto_test', estado='Pendiente')

    def test_crear_comite(self):
        c = Client()
        c.login(username='super', password='super')
        url = reverse('solicitudCambio.views.crear_comite', args=[self.proyecto.id])
        diccionario = {'primer_integrante': self.user.id, 'segundo_integrante': self.user2.id,
                       'tercer_integrante': self.user3.id, 'proyecto': self.proyecto.id, 'estado': 'ACT'}
        response = c.post(url, diccionario, follow=True)
        url_retorno = '/home/'
        self.assertRedirects(response, url_retorno)