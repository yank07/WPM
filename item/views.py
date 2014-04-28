from django import forms
from django.forms.util import ErrorList
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import UpdateView
from django_tables2 import RequestConfig
import eav
from eav.models import Attribute, Entity, Value
from eav.registry import Registry
from TipoItemApp.models import TipoItem
from TipoItemApp.tables import TipoItemTable, AtributoTable
from item.forms import add_item_form, asignar_valor_item_form
from item.models import Item
from proyecto.models import Fase
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory

@login_required
def add_item(request):
    """
    Vista para crear un item
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    context = RequestContext(request)
    if request.method == 'POST':
        form = add_item_form(request.POST,request.FILES)
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
            #archivo = request.FILES['file']
            t=TipoItem.objects.filter(fases__id__exact=faseID,id=tipoitemID)
            if t.__len__()==0:
                errors=form._errors.setdefault("fase",ErrorList())
                errors.append("Elegir fases que posean el tipo de item seleccionado")
                return render_to_response('add_item.html', {'form': form}, context)

            if int(complejidad) > 100 or int(complejidad) < 1:
                errors=form._errors.setdefault("complejidad",ErrorList())
                errors.append("Ingrese un valor comprendido entre [1-100]")
                return render_to_response('add_item.html', {'form': form}, context)
            form.save()
            return HttpResponseRedirect('/item/')
        else:
            print form.errors
    else:
        form = add_item_form()
    return render_to_response('add_item.html', {'form': form}, context)

class value_form(forms.Form):
    valor = forms.CharField()

@login_required
def asignar_valor_item(request):
    """
    Vista para asignar valores a los atributos del item
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    attrs=Attribute.objects.all()
    item=Item.objects.first()
    print item.id
    context = RequestContext(request)
    if request.method == 'POST':
        form = asignar_valor_item_form(request.POST,atributos=attrs)

        if form.is_valid():
            for attr in attrs:
                valor = request.POST.__getitem__(attr.name)
                Value.objects.create(entity=item, attribute=attr,value=valor)

            return HttpResponseRedirect('/item/')
        else:
            print form.errors
    else:
        form = asignar_valor_item_form(atributos=attrs)
    return render_to_response('asignar_valor_item.html', {'form': form}, context)