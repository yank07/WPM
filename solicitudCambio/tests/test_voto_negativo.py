from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User
from eav.models import Attribute
from TipoItemApp.models import TipoItem
from item.models import Item
from proyecto.models import Proyecto
from solicitudCambio.models import Solicitud, Comite

__author__ = 'ccaballero'


class TestVotoNegativo(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.user2 = User.objects.create_user('user2', 'lennon@thebeatles.com', 'user2')
        self.user3 = User.objects.create_user('user3', 'lennon@thebeatles.com', 'user3')
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna',
                                                presupuesto=111, nombre='proyecto_test', estado='Pendiente')
        self.fase = self.proyecto.fases.first()
        self.proyecto.miembros.add(self.user)
        self.attr1 = Attribute.objects.create(name='att1', datatype='int', required=False)
        self.tipoitem = TipoItem.objects.create(nombre='tipo1', descripcion='desc', observacion='ninguna')
        self.tipoitem.atributos.add(self.attr1)
        self.tipoitem.fases.add(self.fase)
        self.item = Item.objects.create(nombre='item1', tipoitem=self.tipoitem, fase=self.fase, complejidad=10,
                                        costo=10, estado='BLOQ')
        self.solicitud = Solicitud.objects.create(item=self.item, usuario=self.user, impacto=20, motivo='test',
                                                  estado='PEN', fecha_caducar='2014-06-16')
        self.comite = Comite.objects.create(proyecto=self.proyecto, primer_integrante=self.user,
                                            segundo_integrante=self.user2, tercer_integrante=self.user3, estado='ACT')

    def test_voto_negativo(self):
        c = Client()
        c.login(username='super', password='super')
        url = reverse('solicitudCambio.views.voto_negativo', args=[self.solicitud.id])
        response = c.get(url)
        url_retorno = reverse('solicitudCambio.views.listar_solicitudes')
        self.assertRedirects(response, url_retorno)