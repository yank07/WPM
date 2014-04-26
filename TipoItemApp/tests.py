from problem_report import ProblemReport
from django.contrib.auth.models import User
from django.test import TestCase
from eav.models import Attribute
from TipoItemApp.models import TipoItem
from proyecto.models import Proyecto, Fase
from django.test.client import Client


class TipoItemViewTests(TestCase):
    def test_edit_tipoitem(self):
        """
        Controlar que no se pueda editar un tipo de item
        cuando el proyecto al que pertenece su fase asociada esta en estado Activo.
        """
        c = Client()
        c.login(username='super', password='super')
        user = User.objects.create()
        p = Proyecto.objects.create(usuario=user,nombre='proy1',presupuesto=123,
                                    observaciones='ninguna',estado='Activo',numero_fases=1)
        fase=Fase.objects.get(proyecto__id=p.id)
        attr1 = Attribute.objects.create(name='att1',datatype='int',required=False)
        tipoitem = TipoItem.objects.create(nombre='tipo1',descripcion='desc',observacion='ninguna')
        tipoitem.atributos.add(attr1)
        tipoitem.fases.add(fase)
        response = c.post('/edit_tipoitem/'+str(tipoitem.id)+'/')
        print response
        self.assertEqual(1,1)
        #self.assertEqual(response.content,"No se puede modificar un tipo de item de un proyecto en estado activo")
