from django.contrib import admin

from proyecto.models import *

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]

admin.site.register(Proyecto, ProyectoAdmin)
# Register your models here.
