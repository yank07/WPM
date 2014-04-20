__author__ = 'ccaballero'

import django_tables2 as tables
from django.contrib.auth.models import User, Group


class UserTable(tables.Table):
    username = tables.Column(verbose_name="Nombre de Usuario")
    editar = tables.TemplateColumn(template_name="columna_usuario.html", sortable=False)

    class Meta:
        model = User
        attrs = {"class": "paleblue"}
        fields = ("username", "first_name" , "last_name", "email")
        sequence = ("username", "first_name" , "last_name", "email")

class GroupTable (tables.Table):
    name = tables.Column(verbose_name="Nombre del Grupo")
    editar = tables.TemplateColumn(template_name="columna_rol.html", sortable=False)

    class Meta:
        model = Group
        attrs = {"class": "paleblue"}
        exclude = ['id']
        # fields = ("name")
        # sequence = ("name")