from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from TipoItemApp.models import TipoItem
from proyecto.models import Proyecto, Fase
from eav.models import Attribute
from item.models import Item

__author__ = 'ccaballero'


class TestAsignar_valor_item(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna',
                                                presupuesto=111, nombre='proyecto_test', estado='Pendiente')
        self.fase = self.proyecto.fases.first()
        #crear atributo
        self.attr1 = Attribute.objects.create(name='att1',datatype='int',required=False)
        #crear tipo item
        self.tipoitem = TipoItem.objects.create(nombre='tipo1',descripcion='desc',observacion='ninguna')
        #asignar atributo a tipo item
        self.tipoitem.atributos.add(self.attr1)
        #asignar tipo item a la fase
        self.tipoitem.fases.add(self.fase)
        self.item = Item.objects.create(nombre='item1', tipoitem=self.tipoitem, fase=self.fase, complejidad=10,
                                        costo=10)



    def test_asignar_valor_item(self):
        c = Client()
        #iniciamos sesion
        c.login(username='super', password='super')
        url = reverse('item.views.asignar_valor_item', args=[self.item.id])
        diccionario = {'attr1': 10}
        response = c.post(url, diccionario, follow=True)
        url_retorno = '/item/listar_item/' + str(self.fase.id) + '/'
        self.assertRedirects(response, url_retorno)