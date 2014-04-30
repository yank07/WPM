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
from item.forms import add_item_form, asignar_valor_item_form, ItemFilter
from item.models import Item
from item.tables import ItemTable
from proyecto.models import Fase
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
import time

@login_required
def add_item(request,id_fase):
    """
    Vista para crear un item
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    context = RequestContext(request)
    if request.method == 'POST':
        form = add_item_form(request.POST,request.FILES)

        if form.is_valid():
            #nombre = request.POST.__getitem__('nombre')
            #tipoitemID = request.POST.__getitem__('tipoitem')
            #tipoitem = TipoItem.objects.get(id=tipoitemID)
            faseID = request.POST.__getitem__('fase')
            #fase = TipoItem.objects.get(fases__id=faseID)
            complejidad = request.POST.__getitem__('complejidad')
            #costo = request.POST.__getitem__('costo')
            #descripcion = request.POST.__getitem__('descripcion')
            #observacion = request.POST.__getitem__('observacion')
            #archivo = request.FILES['file']
            # t=TipoItem.objects.filter(fases__id__exact=faseID,id=tipoitemID)
            # if t.__len__()==0:
            #     errors=form._errors.setdefault("fase",ErrorList())
            #     errors.append("Elegir fases que posean el tipo de item seleccionado")
            #     return render_to_response('add_item.html', {'form': form,'id_fase':id_fase}, context)
            if faseID != id_fase:
                errors=form._errors.setdefault("fase",ErrorList())
                errors.append("Este valor es de solo lectura")
                return render_to_response('add_item.html', {'form': form,'id_fase':id_fase}, context)

            if int(complejidad) > 100 or int(complejidad) < 1:
                errors=form._errors.setdefault("complejidad",ErrorList())
                errors.append("Ingrese un valor comprendido entre [1-100]")
                return render_to_response('add_item.html', {'form': form,'id_fase':id_fase}, context)
            form.save()
            return HttpResponseRedirect('/item/listar_item/'+id_fase)
        else:
            print form.errors
            form.fields["tipoitem"].queryset = TipoItem.objects.filter(fases__id=id_fase)
    else:
        form = add_item_form(initial={'fase':id_fase})
        form.fields["tipoitem"].queryset = TipoItem.objects.filter(fases__id=id_fase)
        print form.as_table()

    return render_to_response('add_item.html', {'form': form,'id_fase':id_fase}, context)

class value_form(forms.Form):
    valor = forms.CharField()

@login_required
def asignar_valor_item(request,id_item):
    """
    Vista para asignar valores a los atributos del item
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    #attrs=Attribute.objects.all()
    item=Item.objects.get(id=id_item)
    tipoitem_id=item.tipoitem_id
    attr_list = Attribute.objects.filter(tipoitem__id__exact=tipoitem_id)
    context = RequestContext(request)
    if request.method == 'POST':
        form = asignar_valor_item_form(request.POST,atributos=attr_list)

        if form.is_valid():
            for attr in attr_list:
                valor = request.POST.__getitem__(attr.name)
                if Value.objects.filter(entity_id=item.id, attribute_id=attr.id).__len__() == 0:
                    Value.objects.create(entity=item, attribute=attr,value=valor)
                else:
                    value = Value.objects.get(entity_id=item.id, attribute_id=attr.id)
                    value.value=valor
                    value.save()
            id_fase = item.fase_id
            return HttpResponseRedirect('/item/listar_item/'+str(id_fase))
        else:
            print form.errors
    else:
        attr_value_dict=[]
        try:
            for attr in attr_list:
                value = Value.objects.get(entity_id=id_item, attribute_id=attr.id)
                valor=value.value
                if attr.datatype=='date':
                    iso=valor.isoformat()
                    tokens = iso.strip().split("T")
                    valor = "%s" % (tokens[0])


                attr_value = attr.name, valor
                attr_value_dict.append(attr_value)
        except Value.DoesNotExist:
            print 'Ningun valor'
        attr_value_dict = dict(attr_value_dict)
        print attr_value_dict
        form = asignar_valor_item_form(atributos=attr_list, initial=attr_value_dict)
    return render_to_response('asignar_valor_item.html', {'form': form,'id_item':id_item}, context)

def listar_item(request,id_fase):
    """
    Vista para listar los items de una fase
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    f = ItemFilter(request.GET, queryset=Item.objects.filter(fase_id=id_fase))
    lista = ItemTable(f)

    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('listar_item.html', {'lista': lista , 'filter': f,'id_fase':id_fase},
                              context_instance=RequestContext(request))
