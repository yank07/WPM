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
    """
    Clase de test para la vista edit_tipoitem
    """

    def setUp(self):
        """
        Metodo de preparacion
        """
        #creamos usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        #creamos proyecto
        self.p = Proyecto.objects.create(usuario=self.user,nombre='proy1',presupuesto=123,
                                    observaciones='ninguna',estado='Activo',numero_fases=1)
        #obtenemos fase
        self.fase = Fase.objects.get(proyecto__id=self.p.id)
        #creamos atributo
        self.attr1 = Attribute.objects.create(name='att1',datatype='int',required=False)
        #creamos tipo item
        self.tipoitem = TipoItem.objects.create(nombre='tipo1',descripcion='desc',observacion='ninguna')
        #asignamos atributo a tipo item
        self.tipoitem.atributos.add(self.attr1)
        #asignamos tipo item a fase
        self.tipoitem.fases.add(self.fase)

    def test_edit_tipoitem(self):
        """
        Controlar que no se pueda editar un tipo de item
        cuando el proyecto al que pertenece su fase asociada esta en estado Activo.
        """
        c = Client()
        #iniciar sesion
        c.login(username='super', password='super')
        #obtener url
        url = reverse('edit_tipoitem', args=[self.tipoitem.id])
        #hacer POST
        response = c.post(url, {'nombre': 'tipoitem', 'descripcion': 'test', 'observacion': 'test',
                                    'atributos': self.attr1.id, 'fases': self.fase.id}, follow=True)
        #buscamos el texto de error
        text = response.content
        m = re.search('<strong>(.+?)</strong>', text)
        found = m.group(1)
        #la vista pasa si se encuentra el mensaje de error
        self.assertEqual(found, 'No se puede modificar un tipo de item de un proyecto en estado activo')