from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from eav.models import Attribute
from TipoItemApp.models import TipoItem
from proyecto.models import Proyecto, Fase

__author__ = 'ccaballero'


class TestDelete_tipoitem(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.p = Proyecto.objects.create(usuario=self.user,nombre='proy1',presupuesto=123,
                                    observaciones='ninguna',estado='Activo',numero_fases=1)
        self.fase = Fase.objects.get(proyecto__id=self.p.id)
        self.attr1 = Attribute.objects.create(name='att1',datatype='int',required=False)
        self.tipoitem = TipoItem.objects.create(nombre='tipo1',descripcion='desc',observacion='ninguna')
        self.tipoitem.atributos.add(self.attr1)
        self.tipoitem.fases.add(self.fase)

    def test_delete_tipoitem(self):
        c = Client()
        c.login(username='super', password='super')
        url = reverse('delete_tipoitem', args=[self.tipoitem.id])
        response = c.post(url, follow=True)
        self.assertRedirects(response, '/admin_tipoitem/')