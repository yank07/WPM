from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User
from eav.models import Attribute
from TipoItemApp.models import TipoItem
from item.models import Item
from proyecto.models import Proyecto

__author__ = 'ccaballero'


class TestReporteVersionesItem(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna',
                                                presupuesto=111, nombre='proyecto_test', estado='Pendiente')
        self.fase = self.proyecto.fases.first()
        self.fase = self.proyecto.fases.first()
        self.attr1 = Attribute.objects.create(name='att1',datatype='int',required=False)
        self.tipoitem = TipoItem.objects.create(nombre='tipo1',descripcion='desc',observacion='ninguna')
        self.tipoitem.atributos.add(self.attr1)
        self.tipoitem.fases.add(self.fase)
        self.item = Item.objects.create(nombre='item1', tipoitem=self.tipoitem, fase=self.fase, complejidad=10,
                                        costo=10)

    def test_reporte_versiones_item(self):
        c = Client()
        c.login(username='super', password='super')
        url = reverse('reportes.views.reporte_versiones_item', args=[self.item.id])
        response = c.get(url, follow=True)
        self.assertEqual(response.status_code, 200)