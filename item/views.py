from django import forms
from django.db.models import Max
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
from item.forms import add_item_form, asignar_valor_item_form, ItemFilter, edit_item_form, crear_sucesor_form
from item.models import Item, relaciones
from item.tables import ItemTable, RevivirItemTable, RevertirItemTable
from proyecto.models import Fase, Proyecto
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
    #revisar por que id ya existe (algunas veces)
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
            rango_valor_inicio = Value.objects.last().id
            rango_valor_final = 0
            first=True
            for attr in attr_list:
                print attr
                valor = request.POST.__getitem__(attr.name)
                print valor
                Value.objects.create(entity=item, attribute=attr, value=valor)
                id = Value.objects.last().id
                if first:
                    rango_valor_inicio = id
                    first=False
                rango_valor_final = id
            #endfor
            item_nuevo = item
            item_nuevo.version=item_nuevo.version+1
            item_nuevo.rango_valor_inicio=rango_valor_inicio
            item_nuevo.rango_valor_final=rango_valor_final
            item_nuevo.save()
            id_fase = item.fase_id
            return HttpResponseRedirect('/item/listar_item/'+str(id_fase))
        else:
            print form.errors
    else:
        attr_value_dict=[]
        if item.rango_valor_inicio < item.rango_valor_final:
            valor_id=item.rango_valor_inicio
            for attr in attr_list:
                value = Value.objects.get(id=valor_id)
                valor=value.value
                if attr.datatype=='date':
                    iso=valor.isoformat()
                    tokens = iso.strip().split("T")
                    valor = "%s" % (tokens[0])
                attr_value = attr.name, valor
                attr_value_dict.append(attr_value)
                valor_id = valor_id + 1
            #endfor
        #endif
        attr_value_dict = dict(attr_value_dict)
        form = asignar_valor_item_form(atributos=attr_list, initial=attr_value_dict)
    return render_to_response('asignar_valor_item.html', {'form': form,'id_item':id_item}, context)


def listar_item(request,id_fase):
    """
    Vista para listar los items de una fase
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    itemXfase = Item.objects.filter(fase_id=id_fase)
    queryset=itemXfase.exclude(estado='ELIM')

    f = ItemFilter(request.GET, queryset=queryset)
    lista = ItemTable(f)

    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('listar_item.html', {'lista': lista , 'filter': f,'id_fase':id_fase},
                              context_instance=RequestContext(request))

def edit_item(request,id_item):
    """
    Vista para modificar los valores de un item
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    context = RequestContext(request)
    item_original = Item.objects.get(id=id_item)
    if request.method == 'POST':
        form = edit_item_form(request.POST,request.FILES)
        if form.is_valid():
            change=False
            item_nuevo=item_original
            complejidad = request.POST.__getitem__('complejidad')

            item_nuevo.complejidad=complejidad
            if int(complejidad) > 100 or int(complejidad) < 1:
                errors=form._errors.setdefault("complejidad",ErrorList())
                errors.append("Ingrese un valor comprendido entre [1-100]")
                return render_to_response('add_item.html', {'form': form,'id_item':id_item}, context)
            if complejidad != item_original.complejidad:
                change = True

            costo = request.POST.__getitem__('costo')
            item_nuevo.costo=costo
            if costo != item_original.costo:
                change = True

            descripcion = request.POST.__getitem__('descripcion')
            item_nuevo.descripcion=descripcion
            if descripcion != item_original.descripcion:
                change = True

            observacion = request.POST.__getitem__('observacion')
            item_nuevo.observacion=observacion
            if observacion != item_original.observacion:
                change = True

            estado = request.POST.__getitem__('estado')
            item_nuevo.estado=estado

            file = form.cleaned_data['archivo']
            if file is not None:
                change=True
                #print file.name
                item_nuevo.archivo=file

            if change:
                item_nuevo.id = Item.objects.last().id+1
                item_nuevo.version=item_nuevo.version+1

            item_nuevo.save()
            if change==False:
                item_nuevo.history.last().delete()

            return HttpResponseRedirect('/item/listar_item/'+str(item_original.fase_id))
        else:
            print form.errors
    else:
        dictionary = {'complejidad': item_original.complejidad,'costo': item_original.costo,
                      'estado': item_original.estado,'descripcion': item_original.descripcion,
                      'observacion': item_original.observacion}
        form = edit_item_form(initial=dictionary)

    return render_to_response('edit_item.html', {'form': form,'id_item':id_item}, context)

def listar_item_muerto(request,id_fase):
    """
    Vista que lista los items muertos para posterior resurreccion
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    itemXfase = Item.objects.filter(fase_id=id_fase)
    queryset=itemXfase.filter(estado='ELIM')

    f = ItemFilter(request.GET, queryset=queryset)
    lista = RevivirItemTable(f)

    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('listar_item_muerto.html', {'lista': lista , 'filter': f,'id_fase':id_fase},
                              context_instance=RequestContext(request))

def revivir_item(request,id_item):
    """
    Vista para revivir item
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    item = Item.objects.get(id=id_item)
    item.estado='ACT'
    item.save()
    #un cambio de estado no implica una nueva version del item
    item.history.last().delete()
    return HttpResponseRedirect('/item/listar_item/'+str(item.fase_id))

def crear_sucesor(request,id_fase):
    """
    Vista para crear una relacion Sucesor
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    context = RequestContext(request)
    error=False
    if request.method == 'POST':
        form = crear_sucesor_form(request.POST)
        if form.is_valid():
            item_origen_id = request.POST.__getitem__('items_origen')
            item_destino_id = request.POST.__getitem__('items_destino')
            print item_origen_id
            print item_destino_id
            relaciones.objects.create(tipo_relacion='SUC',item_origen_id=item_origen_id,item_destino_id=item_destino_id)
            return HttpResponseRedirect('/item/listar_item/'+id_fase)
        else:
            print form.errors
    else:
        form = crear_sucesor_form()
        fase=Fase.objects.get(id=id_fase)
        fases=Fase.objects.filter(proyecto_id=fase.proyecto_id)
        id_fase_ultimo = fases.aggregate(Max('id'))
        if str(id_fase) == str(id_fase_ultimo['id__max']):
            error=True
        else:
            form.fields["items_origen"].queryset = Item.objects.filter(fase__id=id_fase)
            form.fields["items_destino"].queryset = Item.objects.filter(fase__id=str(int(id_fase)+1))
    return render_to_response('crear_sucesor.html', {'form': form,'id_fase':id_fase,'error':error}, context)

def crear_hijo(request,id_fase):
    """
    Vista para crear una relacion Sucesor
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    context = RequestContext(request)
    error=False
    if request.method == 'POST':
        form = crear_sucesor_form(request.POST)
        if form.is_valid():
            item_origen_id = request.POST.__getitem__('items_origen')
            item_destino_id = request.POST.__getitem__('items_destino')
            if item_destino_id == item_origen_id:
                errors=form._errors.setdefault("items_destino",ErrorList())
                errors.append("Un item no puede tener como hijo a si mismo")
                form.fields["items_origen"].queryset = Item.objects.filter(fase__id=id_fase)
                form.fields["items_destino"].queryset = Item.objects.filter(fase__id=id_fase)
                return render_to_response('crear_hijo.html', {'form': form,'id_fase':id_fase}, context)
            #controlar que no se cree la misma relacion
            if relaciones.objects.filter(item_origen_id=item_origen_id, item_destino_id=item_destino_id).__len__() > 0:
                errors=form._errors.setdefault("items_destino",ErrorList())
                errors.append("Esta relacion ya existe")
                form.fields["items_origen"].queryset = Item.objects.filter(fase__id=id_fase)
                form.fields["items_destino"].queryset = Item.objects.filter(fase__id=id_fase)
                return render_to_response('crear_hijo.html', {'form': form,'id_fase':id_fase}, context)
            if relaciones.objects.filter(item_origen_id=item_origen_id, item_destino_id=item_destino_id).__len__() == 0:
                if relaciones.objects.filter(item_origen_id=item_destino_id, item_destino_id=item_origen_id).__len__()>0:
                    errors=form._errors.setdefault("items_destino",ErrorList())
                    errors.append("Un item no puede ser hijo de su propio padre o viceversa")
                    form.fields["items_origen"].queryset = Item.objects.filter(fase__id=id_fase)
                    form.fields["items_destino"].queryset = Item.objects.filter(fase__id=id_fase)
                    return render_to_response('crear_hijo.html', {'form': form,'id_fase':id_fase}, context)
                else:
                    relaciones.objects.create(tipo_relacion='HIJ',
                                      item_origen_id=item_origen_id,
                                      item_destino_id=item_destino_id)
            return HttpResponseRedirect('/item/listar_item/'+id_fase)
        else:
            print form.errors
    else:
        form = crear_sucesor_form()
        form.fields["items_origen"].queryset = Item.objects.filter(fase__id=id_fase)
        form.fields["items_destino"].queryset = Item.objects.filter(fase__id=id_fase)
    return render_to_response('crear_hijo.html', {'form': form,'id_fase':id_fase}, context)

def listar_versiones(request, id_item):
    """
    Vista para ver las versiones anteriores de un item
    @param request: Peticion HTTP, id del item
    @return renderiza el form correspondiente
    """
    item = Item.objects.get(id=id_item)
    queryset = item.history

    f = ItemFilter(request.GET, queryset=queryset)
    lista = RevertirItemTable(f)

    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('historial_item.html', {'lista': lista , 'filter': f,'id_item':id_item},
                              context_instance=RequestContext(request))

def revertir_item(request, id_item, version):
    """
    Vista para revertir un item a una version anterior
    @param request: Peticion HTTP, id del item
    @return renderiza el form correspondiente
    """
    item = Item.objects.get(id=id_item)
    item_nuevo = item.history.get(id=id_item,version=version)
    item.copy(item_nuevo)
    item.save()
    item_nuevo.delete()
    return HttpResponseRedirect('/item/listar_item/'+str(item.fase_id))