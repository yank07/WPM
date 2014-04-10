# from unittest import TestCase
from django.test import TestCase
from principal.models import Proyecto

__author__ = 'ccaballero'


class TestAdd_proyecto(TestCase):
    def test_add_proyecto(self):
        proy1 = Proyecto(1, 1, 'test1', 10, 'ninguna', 1)
        proy1.save()
        proy2 = Proyecto.objects.all().get(nombre='test1')
        self.assertEqual(proy1.nombre, proy2.nombre)