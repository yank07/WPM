from django.contrib import admin
from principal.models import *

# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]

admin.site.register(Proyecto, ProyectoAdmin)







