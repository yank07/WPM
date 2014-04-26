from django.forms.util import ErrorList
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import UpdateView
from django_tables2 import RequestConfig
import eav
from eav.models import Attribute, Entity
from eav.registry import Registry
from TipoItemApp.models import TipoItem
from TipoItemApp.tables import TipoItemTable, AtributoTable
from item.forms import add_item_form
from proyecto.models import Fase

from django.contrib.auth.decorators import login_required

@login_required
def add_item(request):
    """
    Vista para crear un item
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    context = RequestContext(request)
    if request.method == 'POST':
        form = add_item_form(request.POST)
        if form.is_valid():
            nombre = request.POST.__getitem__('nombre')
            tipoitemID = request.POST.__getitem__('tipoitem')
            tipoitem = TipoItem.objects.get(id=tipoitemID)
            faseID = request.POST.__getitem__('fase')
            #fase = TipoItem.objects.get(fases__id=faseID)
            complejidad = request.POST.__getitem__('complejidad')
            costo = request.POST.__getitem__('costo')
            descripcion = request.POST.__getitem__('descripcion')
            observacion = request.POST.__getitem__('observacion')
            archivo = request.POST.__getitem__('archivo')
            t=TipoItem.objects.filter(fases__id__exact=faseID,id=tipoitemID)
            if t.__len__()==0:
                errors=form._errors.setdefault("fase",ErrorList())
                errors.append("Elegir fases que posean el tipo de item seleccionado")
                return render_to_response('add_item.html', {'form': form}, context)
            
            if int(complejidad) > 100 or int(complejidad) < 1:
                errors=form._errors.setdefault("complejidad",ErrorList())
                errors.append("Ingrese un valor comprendido entre [1-100]")
                return render_to_response('add_item.html', {'form': form}, context)
            form.save(commit=True)
            return HttpResponseRedirect('/item/')
        else:
            print form.errors
    else:
        form = add_item_form()
    return render_to_response('add_item.html', {'form': form}, context)
