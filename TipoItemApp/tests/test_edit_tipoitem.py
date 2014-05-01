from unittest import TestCase
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from TipoItemApp.models import TipoItem
from proyecto.models import Proyecto, Fase
from eav.models import Attribute
import re

__author__ = 'ccaballero'


class TestEdit_tipoitem(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        self.p = Proyecto.objects.create(usuario=self.user,nombre='proy1',presupuesto=123,
                                    observaciones='ninguna',estado='Activo',numero_fases=1)
        self.fase = Fase.objects.get(proyecto__id=self.p.id)
        self.attr1 = Attribute.objects.create(name='att1',datatype='int',required=False)
        self.tipoitem = TipoItem.objects.create(nombre='tipo1',descripcion='desc',observacion='ninguna')
        self.tipoitem.atributos.add(self.attr1)
        self.tipoitem.fases.add(self.fase)

    def test_edit_tipoitem(self):
        """
        Controlar que no se pueda editar un tipo de item
        cuando el proyecto al que pertenece su fase asociada esta en estado Activo.
        """
        c = Client()
        c.login(username='super', password='super')
        url = reverse('edit_tipoitem', args=[self.tipoitem.id])
        response = c.post(url, {'nombre': 'tipoitem', 'descripcion': 'test', 'observacion': 'test',
                                    'atributos': self.attr1.id, 'fases': self.fase.id}, follow=True)
        text = response.content
        m = re.search('<strong>(.+?)</strong>', text)
        found = m.group(1)
        self.assertEqual(found, 'No se puede modificar un tipo de item de un proyecto en estado activo')