from unittest import TestCase
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from proyecto.models import Proyecto

__author__ = 'ccaballero'


class TestDelete_proyecto(TestCase):
    """
    Clase de implementacion de test para la vista delete_proyecto
    """

    def setUp(self):
        """
        Metodo de preparacion de test
        """
        #creamos un usuario
        self.user = User.objects.create_user('super', 'lennon@thebeatles.com', 'super')
        #creamos un proyecto
        self.proyecto = Proyecto.objects.create(numero_fases=2, usuario=self.user, observaciones='ninguna', presupuesto=111, nombre='proyecto_test', estado='Pendiente')


    def test_delete_proyecto(self):
        c = Client()
        #iniciamos sesion
        c.login(username='super', password='super')
        #obtenemos el id del proyecto creado
        p = Proyecto.objects.get(nombre='proyecto_test')
        #obtenemos la url de la vista
        url = reverse('delete_proyecto', args=[p.id])
        #hacemos un POST a esa url
        response = c.post(url, follow=True)
        #el test pasa si la vista nos redirige a /admin_proyectos
        self.assertRedirects(response, '/admin_proyectos/')