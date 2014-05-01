from django.test import TestCase
from WPM.settings import RUTA_PROYECTO, MEDIA_ROOT
from item.models import Item
from django.test.client import Client
import os
from proyecto.models import Fase


class ItemViewTests(TestCase):
    def test_upload_file(self):
        path=os.path.join(MEDIA_ROOT,'files')
        f = open('archivo','w')
        f.write('Este archivo debe guardarse en PROJECT_HOME/uploaded_files/files')
        #item = Item.objects.create(nombre='item1',tipoitem_id=1,fase_id=1,complejidad=50,costo=123,estado='ACT',descripcion='ninguna',)
        c = Client()
        Fase.objects.create()
        response = c.post('/item/add_item/1', {'username': 'john', 'password': 'smith'})