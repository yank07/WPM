
from django import forms
from django.contrib.auth.models import Permission, User
from django.db.models import Max, Min
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
from item.forms import add_item_form, asignar_valor_item_form, ItemFilter, edit_item_form, crear_sucesor_form, \
    delete_relacion_form
from item.models import Item, relaciones
from item.tables import ItemTable, RevivirItemTable, RevertirItemTable
from proyecto.models import Fase, Proyecto
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
import time
from django.db import IntegrityError

import networkx as nx



@login_required
def add_item(request, id_fase):
    """
    Vista para crear un item
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    #revisar por que id ya existe (algunas veces)
    context = RequestContext(request)
    fase = Fase.objects.get(id=id_fase)
    if not es_miembro(request.user.id, fase.proyecto.id):
        #error: no es miembro
        mensaje = 'Usted no es miembro del proyecto, no puede crear un item'
        return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)
    if request.method == 'POST':
        form = add_item_form(request.POST, request.FILES)

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
            # t=TipoItem.objects.filter(fases__id__exact=faseID,id=tipoitemID)
            # if t.__len__()==0:
            #     errors=form._errors.setdefault("fase",ErrorList())
            #     errors.append("Elegir fases que posean el tipo de item seleccionado")
            #     return render_to_response('add_item.html', {'form': form,'id_fase':id_fase}, context)
            if faseID != id_fase:
                errors = form._errors.setdefault("fase", ErrorList())
                errors.append("Este valor es de solo lectura")
                return render_to_response('add_item.html', {'form': form, 'id_fase': id_fase}, context)

            if int(complejidad) > 100 or int(complejidad) < 1:
                errors = form._errors.setdefault("complejidad", ErrorList())
                errors.append("Ingrese un valor comprendido entre [1-100]")
                return render_to_response('add_item.html', {'form': form, 'id_fase': id_fase}, context)

            #item = Item.objects.create(nombre=nombre,fase=faseID,costo=costo,complejidad=complejidad,descripcion=descripcion,archivo=archivo,observacion=observacion)
            #item.tipoitem.add(tipoitem)
            try:
                item = form.save()
            except IntegrityError:
                errors = form._errors.setdefault("nombre", ErrorList())
                errors.append("El nombre del Item debe ser unico")
                return render_to_response('add_item.html', {'form': form, 'id_fase': id_fase}, context)

            item_origen_id_list = request.POST.getlist('antecesor')
            for item_origen_id in item_origen_id_list:
                item_origen = Item.objects.get(id=item_origen_id)
                relaciones.objects.create(tipo_relacion='SUC', item_origen_id=item_origen_id, item_destino_id=item.id,
                                          item_origen_version=item_origen.version, item_destino_version=item.version)
            item_origen_id_list = request.POST.getlist('padre')
            for item_origen_id in item_origen_id_list:
                if es_consistente(id_fase) == True:
                    item_origen = Item.objects.get(id=item_origen_id)
                    relaciones.objects.create(tipo_relacion='HIJ', item_origen_id=item_origen_id,
                                              item_destino_id=item.id,
                                              item_origen_version=item_origen.version,
                                              item_destino_version=item.version)
                else:
                    errors = form._errors.setdefault("padre", ErrorList())
                    errors.append("INCONSISTENCIA: Se crean ciclos en el grafo de relaciones!")
                    return render_to_response('add_item.html', {'form': form, 'id_fase': id_fase}, context)

            return HttpResponseRedirect('/item/listar_item/'+id_fase)
        else:
            print form.errors
            form.fields["tipoitem"].queryset = TipoItem.objects.filter(fases__id=id_fase)
            form.fields["antecesor"].queryset = Item.objects.filter(fase__id=int(id_fase) - 1, estado="BLOQ")
            form.fields["padre"].queryset = Item.objects.filter(fase__id=int(id_fase)).exclude(estado='ELIM')

    else:
        form = add_item_form(initial={'fase': id_fase})
        print id_fase

        fases=Fase.objects.filter(proyecto_id=fase.proyecto_id)
        fase = Fase.objects.get(id=id_fase)
        fases = Fase.objects.filter(proyecto_id=fase.proyecto_id)
        id_fase_primero = fases.aggregate(Min('id'))
        print id_fase_primero
        form.fields["padre"].queryset = Item.objects.filter(fase__id=int(id_fase)).exclude(estado='ELIM')
        if id_fase_primero != id_fase:
            print "no primero"
            fase_anterior = int(id_fase) - 1
            form.fields["antecesor"].queryset = Item.objects.filter(fase__id=fase_anterior, estado="BLOQ")
        else:
            form.fields["antecesor"].queryset = Item.objects.none()
        form.fields["tipoitem"].queryset = TipoItem.objects.filter(fases__id=id_fase)

        # print form.as_table()

    return render_to_response('add_item.html', {'form': form,'id_fase':id_fase,
                                                'proy_nombre': fase.proyecto.nombre, 'id_proyecto': fase.proyecto.id,
                                                'nombre_fase': fase.nombre}, context)


class value_form(forms.Form):
    valor = forms.CharField()


@login_required
def asignar_valor_item(request, id_item):
    """
    Vista para asignar valores a los atributos del item
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    item = Item.objects.get(id=id_item)
    tipoitem_id = item.tipoitem_id
    attr_list = Attribute.objects.filter(tipoitem__id__exact=tipoitem_id)
    context = RequestContext(request)
    if request.method == 'POST':
        form = asignar_valor_item_form(request.POST, atributos=attr_list)

        if form.is_valid():
            rango_valor_inicio = 0
            rango_valor_final = 0
            first = True
            #solo se guardaran los valores de los atributos para los cuales se han cargado en el form
            for attr in attr_list:
                if request.POST.__contains__(attr.name):
                    print attr
                    v = request.POST.__getitem__(attr.name)
                    if attr.datatype == 'bool':
                        v = True
                    if v != '':
                        valor = Value.objects.create(entity=item, attribute=attr, value=str(v))
                        id = valor.id
                        if first:
                            rango_valor_inicio = id
                            first = False
                        rango_valor_final = id

                elif attr.datatype == 'bool':
                    v = False
                    valor = Value.objects.create(entity=item, attribute=attr, value=str(v))
                    id = valor.id
                    if first:
                        rango_valor_inicio = id
                        first = False
                    rango_valor_final = id
            #endfor
            item_nuevo = item
            item_nuevo.version = item_nuevo.version + 1
            item_nuevo.rango_valor_inicio = rango_valor_inicio
            item_nuevo.rango_valor_final = rango_valor_final
            item_nuevo.save()
            id_fase = item.fase_id
            return HttpResponseRedirect('/item/listar_item/' + str(id_fase))
        else:
            print form.errors
    else:
        attr_value_dict = []
        if item.rango_valor_inicio <= item.rango_valor_final:
            values = Value.objects.filter(id__in=range(item.rango_valor_inicio,item.rango_valor_final+1))
            attr_list_with_values = [value.attribute for value in values]
            valor_id = item.rango_valor_inicio
            for attr in attr_list_with_values:
                value = Value.objects.get(id=valor_id)
                valor = value.value
                if attr.datatype == 'date':
                    iso = valor.isoformat()
                    tokens = iso.strip().split("T")
                    valor = "%s" % (tokens[0])
                attr_value = attr.name, valor
                attr_value_dict.append(attr_value)
                valor_id = valor_id + 1
                #endfor
        #endif
        attr_value_dict = dict(attr_value_dict)
        form = asignar_valor_item_form(atributos=attr_list, initial=attr_value_dict)
    fase = item.fase
    proyecto = fase.proyecto
    return render_to_response('asignar_valor_item.html', {'form': form, 'id_item': id_item, 'nombre_item': item.nombre,
                                                          'id_fase': fase.id, 'nombre_fase': fase.nombre,
                                                          'id_proyecto': proyecto.id, 'proy_nombre': proyecto.nombre}
                              , context)


@login_required
def listar_item(request, id_fase):
    """
    Vista para listar los items de una fase
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    itemXfase = Item.objects.filter(fase_id=id_fase)



    queryset=itemXfase.exclude(estado='ELIM')
    finalizado = True
    for item in itemXfase:
        if item.estado != "BLOQ":
            finalizado = False
    queryset = itemXfase.exclude(estado='ELIM')

    f = ItemFilter(request.GET, queryset=queryset)
    lista = ItemTable(f)
    fase = Fase.objects.get(id=id_fase)
    id_proyecto = fase.proyecto.id
    proy_nombre = fase.proyecto.nombre

    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
#    return render_to_response('listar_item.html', {'lista': lista, 'filter': f, 'id_fase': id_fase},
    return render_to_response('listar_item.html', {'lista': lista , 'filter': f,'id_fase':id_fase,
                                                   'nombre_fase': fase.nombre, 'id_proyecto': id_proyecto,
                                                   'proy_nombre': proy_nombre},
                              context_instance=RequestContext(request))


@login_required
def edit_item(request, id_item):
    """
    Vista para modificar los valores de un item
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    context = RequestContext(request)
    item_original = Item.objects.get(id=id_item)
    fase = Fase.objects.get(id=item_original.fase_id)

    if not es_miembro(request.user.id, fase.proyecto.id):
        #error: no es miembro
        mensaje = 'Usted no es miembro del proyecto, no puede editar items'
        return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)

    if request.user.has_perm('item.edit_item'):
        if request.method == 'POST':
            form = edit_item_form(request.POST, request.FILES)
            if form.is_valid():
                change = False
                item_nuevo = item_original
                item_nuevo.copy(item_original)
                complejidad_form = request.POST.__getitem__('complejidad')
                complejidad_item = item_original.complejidad

                item_nuevo.complejidad = complejidad_form

                if int(complejidad_form) > 100 or int(complejidad_form) < 1:
                    errors = form._errors.setdefault("complejidad", ErrorList())
                    errors.append("Ingrese un valor comprendido entre [1-100]")
                    return render_to_response('edit_item.html', {'form': form, 'id_item': id_item,
                                                                 'id_fase': fase.id, 'nombre_fase': fase.nombre,
                                                                 'id_proyecto': fase.proyecto.id,
                                                                 'proy_nombre': fase.proyecto.nombre,
                                                                 'nombre_item': item_original.nombre},
                                              context)
                if int(complejidad_item) != int(complejidad_form):
                    change = True

                costo_form = request.POST.__getitem__('costo')
                costo_item = item_original.costo
                item_nuevo.costo = costo_form
                if int(costo_item) != int(costo_form):
                    change = True

                descripcion_form = request.POST.__getitem__('descripcion')
                descripcion_item = item_original.descripcion
                item_nuevo.descripcion = descripcion_form
                if descripcion_form != descripcion_item:
                    change = True

                observacion_form = request.POST.__getitem__('observacion')
                observacion_item = item_original.observacion
                item_nuevo.observacion = observacion_form
                if str(observacion_form) != str(observacion_item):
                    change = True

                estado_form = request.POST.__getitem__('estado')
                estado_item = item_original.estado
                item_nuevo.estado = estado_form
                if estado_form != estado_item:
                    if estado_item == 'ACT' and estado_form == 'APROB':  #esta seccion es la que se debe agregar
                                errors = form._errors.setdefault("estado", ErrorList())
                                errors.append("No se puede pasar un item de estado activo a aprobado sin pasar por revision")
                                return render_to_response('edit_item.html', {'form': form, 'id_item': id_item,
                                                                             'id_fase': fase.id, 'nombre_fase': fase.nombre,
                                                                             'id_proyecto': fase.proyecto.id,
                                                                             'proy_nombre': fase.proyecto.nombre,
                                                                             'nombre_item': item_original.nombre},
                                                          context)
                    if estado_form == 'ELIM':
                        if estado_item != 'ACT':
                            errors = form._errors.setdefault("estado", ErrorList())
                            errors.append("Para que un item pueda ser eliminado, debe estar en un estado activo")
                            return render_to_response('edit_item.html', {'form': form, 'id_item': id_item,
                                                                         'id_fase': fase.id, 'nombre_fase': fase.nombre,
                                                                         'id_proyecto': fase.proyecto.id,
                                                                         'proy_nombre': fase.proyecto.nombre,
                                                                         'nombre_item': item_original.nombre},
                                                      context)
                        sucesores_hijos = relaciones.objects.filter(item_origen_id=id_item, item_origen_version=item_original.version)
                        for sh in sucesores_hijos:
                            sh.delete()
                        antecesore_padres = relaciones.objects.filter(item_destino_id=id_item, item_destino_version=item_original.version)
                        for ap in antecesore_padres:
                            ap.activo = False
                            ap.save()

                file = form.cleaned_data['archivo']
                if file is not None:
                    change = True
                    item_nuevo.archivo = file

                if change:
                    relist = relaciones.objects.filter(item_destino_id=id_item, item_destino_version=item_nuevo.version)
                    for r in relist:
                        relaciones.objects.create(tipo_relacion=r.tipo_relacion, item_origen_id=r.item_origen.id,
                                          item_destino_id=r.item_destino.id,
                                          item_origen_version=r.item_origen_version,
                                          item_destino_version=r.item_destino_version+1)
                    item_nuevo.version = item_nuevo.version + 1

                item_nuevo.save()
                if change == False:
                    item_nuevo.history.last().delete()

                return HttpResponseRedirect('/item/listar_item/' + str(item_original.fase_id))
            else:
                print form.errors
        else:
            dictionary = {'complejidad': item_original.complejidad, 'costo': item_original.costo,
                          'estado': item_original.estado, 'descripcion': item_original.descripcion,
                          'observacion': item_original.observacion}
            form = edit_item_form(initial=dictionary)
    else:
        mensaje = "Usted no puede editar un item, no tiene el permiso"
        return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)

    fase = item_original.fase
    proyecto = fase.proyecto
    return render_to_response('edit_item.html', {'form': form, 'id_item': id_item, 'nombre_item': item_original.nombre,
                                                 'id_fase': fase.id, 'nombre_fase': fase.nombre,
                                                 'id_proyecto': proyecto.id, 'proy_nombre': proyecto.nombre}, context)


@login_required
def listar_item_muerto(request, id_fase):
    """
    Vista que lista los items muertos para posterior resurreccion
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    itemXfase = Item.objects.filter(fase_id=id_fase)
    queryset = itemXfase.filter(estado='ELIM')

    f = ItemFilter(request.GET, queryset=queryset)
    lista = RevivirItemTable(f)
    fase = Fase.objects.get(id=id_fase)

    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('listar_item_muerto.html', {'lista': lista, 'filter': f, 'id_fase': id_fase,
                                                          'proy_nombre': fase.proyecto.nombre,
                                                          'id_proyecto': fase.proyecto.id, 'nombre_fase': fase.nombre},
                              context_instance=RequestContext(request))


@login_required
def revivir_item(request, id_item):
    """
    Vista para revivir item
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    item = Item.objects.get(id=id_item)
    item.estado = 'ACT'
    item.save()
    items = Item.objects.filter(fase__id=item.fase_id).exclude(estado='ELIM')
    itemlist=[]
    for i in items:
        itemlist.append(i)
    itemlist.append(item)
    if es_consistente(id_fase=item.fase_id, nodelist=itemlist):
        ancestros = relaciones.objects.filter(item_destino_id=id_item, item_destino_version=item.version)
        for relacion in ancestros:
            relacion.activo = True
            relacion.save()
        item.history.last().delete()
    else:
        #mostrar la pagina de error cuando no es consistente
        pass

    return HttpResponseRedirect('/item/listar_item/' + str(item.fase_id))


@login_required
def crear_sucesor(request, id_fase):
    """
    Vista para crear una relacion Sucesor
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    context = RequestContext(request)
    error = False
    if request.method == 'POST':
        form = crear_sucesor_form(request.POST)
        if form.is_valid():
            item_origen_id = request.POST.__getitem__('items_origen')
            item_destino_id = request.POST.__getitem__('items_destino')
            item_origen = Item.objects.get(id=item_origen_id)
            item_destino = Item.objects.get(id=item_destino_id)

            relaciones.objects.create(tipo_relacion='SUC', item_origen_id=item_origen_id,
                                      item_destino_id=item_destino_id,
                                      item_origen_version=item_origen.version,
                                      item_destino_version=item_destino.version)
            return HttpResponseRedirect('/item/listar_item/' + id_fase)
        else:
            print form.errors
    else:
        form = crear_sucesor_form()
        fase = Fase.objects.get(id=id_fase)
        fases = Fase.objects.filter(proyecto_id=fase.proyecto_id)
        id_fase_ultimo = fases.aggregate(Max('id'))
        if str(id_fase) == str(id_fase_ultimo['id__max']):
            error = True
        else:
            form.fields["items_origen"].queryset = Item.objects.filter(fase__id=id_fase, estado="BLOQ")
            form.fields["items_destino"].queryset = Item.objects.filter(fase__id=str(int(id_fase) + 1))
    return render_to_response('crear_sucesor.html', {'form': form,'id_fase':id_fase,'error':error,
                                                     'proy_nombre': fase.proyecto.nombre,
                                                     'id_proyecto': fase.proyecto.id,
                                                     'nombre_fase': fase.nombre}, context)


@login_required
def crear_hijo(request, id_fase):
    """
    Vista para crear una relacion Sucesor
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    context = RequestContext(request)
    error = False
    if request.method == 'POST':
        form = crear_sucesor_form(request.POST)
        if form.is_valid():
            item_origen_id = request.POST.__getitem__('items_origen')
            item_destino_id = request.POST.__getitem__('items_destino')
            if item_destino_id == item_origen_id:
                errors = form._errors.setdefault("items_destino", ErrorList())
                errors.append("Un item no puede tener como hijo a si mismo")
                form.fields["items_origen"].queryset = Item.objects.filter(fase__id=id_fase)
                form.fields["items_destino"].queryset = Item.objects.filter(fase__id=id_fase)
                return render_to_response('crear_hijo.html', {'form': form, 'id_fase': id_fase}, context)

            #controlar que no se cree la misma relacion
            if relaciones.objects.filter(item_origen_id=item_origen_id, item_destino_id=item_destino_id).__len__() > 0:
                errors = form._errors.setdefault("items_destino", ErrorList())
                errors.append("Esta relacion ya existe")
                form.fields["items_origen"].queryset = Item.objects.filter(fase__id=id_fase)
                form.fields["items_destino"].queryset = Item.objects.filter(fase__id=id_fase)
                return render_to_response('crear_hijo.html', {'form': form, 'id_fase': id_fase}, context)

            if relaciones.objects.filter(item_origen_id=item_origen_id, item_destino_id=item_destino_id).__len__() == 0:
                if relaciones.objects.filter(item_origen_id=item_destino_id,
                                             item_destino_id=item_origen_id).__len__() > 0:
                    errors = form._errors.setdefault("items_destino", ErrorList())
                    errors.append("Un item no puede ser hijo de su propio padre o viceversa")
                    form.fields["items_origen"].queryset = Item.objects.filter(fase__id=id_fase)
                    form.fields["items_destino"].queryset = Item.objects.filter(fase__id=id_fase)
                    return render_to_response('crear_hijo.html', {'form': form, 'id_fase': id_fase}, context)
                else:
                    item_origen = Item.objects.get(id=item_origen_id)
                    item_destino = Item.objects.get(id=item_destino_id)
                    rel = relaciones.objects.create(tipo_relacion='HIJ',
                                                    item_origen_id=item_origen_id,
                                                    item_destino_id=item_destino_id,
                                                    item_origen_version=item_origen.version,
                                                    item_destino_version=item_destino.version)
                    if es_consistente(id_fase) == False:
                        errors = form._errors.setdefault("items_destino", ErrorList())
                        errors.append("INCONSISTENCIA: Se crean ciclos en el grafo de relaciones!")
                        rel.delete()
                        return render_to_response('add_item.html', {'form': form, 'id_fase': id_fase}, context)
            return HttpResponseRedirect('/item/listar_item/' + id_fase)
        else:
            print form.errors
    else:
        form = crear_sucesor_form()
        fase = Fase.objects.get(id=id_fase)
        form.fields["items_origen"].queryset = Item.objects.filter(fase__id=id_fase)
        form.fields["items_destino"].queryset = Item.objects.filter(fase__id=id_fase)
    return render_to_response('crear_hijo.html', {'form': form,'id_fase':id_fase,
                                                  'proy_nombre': fase.proyecto.nombre,
                                                  'id_proyecto': fase.proyecto.id,
                                                  'nombre_fase': fase.nombre}, context)


@login_required
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
    #return render_to_response('historial_item.html', {'lista': lista, 'filter': f, 'id_item': id_item},
    return render_to_response('historial_item.html', {'lista': lista, 'filter': f, 'id_item': item.id,
                                                      'nombre_item': item.nombre,
                                                      'id_fase': item.fase.id, 'nombre_fase': item.fase.nombre,
                                                      'id_proyecto': item.fase.proyecto.id,
                                                      'proy_nombre': item.fase.proyecto.nombre},
                              context_instance=RequestContext(request))


@login_required
def revertir_item(request, id_item, version):
    """
    Vista para revertir un item a una version anterior
    @param request: Peticion HTTP, id del item
    @return renderiza el form correspondiente
    """
    item = Item.objects.get(id=id_item)
    items = Item.objects.filter(fase__id=item.fase_id).exclude(estado='ELIM')
    item_nuevo = item.history.get(id=id_item, version=version)

    itemlist = []
    for i in items:
        if i.id != id_item:
            itemlist.append(i)
        else:
            itemlist.append(i.history.get(id=id_item, version=version))

    if es_consistente(id_fase=item.fase_id, nodelist=itemlist):
        current = item.version
        item.copy(item_nuevo)
        item.version = current + 1
        r_list = relaciones.objects.filter(item_destino_id=id_item, item_destino_version=version)
        for r in r_list:
            r.item_destino_version = item.version
            r.save()
        item.save()
        item_nuevo.delete()
        return HttpResponseRedirect('/item/listar_item/' + str(item.fase_id))
    else:
        #enviar a una pagina de error
        pass


def es_consistente(id_fase, nodelist=None):
    """
    Implementacion del algoritmo de busqueda de ciclos
    Return True is there is no cicle in the graph.
    """
    MG = nx.MultiDiGraph()
    if nodelist is None:
        items = Item.objects.filter(fase_id=id_fase).exclude(estado='ELIM')
    else:
        items=nodelist

    for item in items:
        MG.add_node(item.id, pos=(item.id, item.id))
        padres = relaciones.objects.filter(item_destino_id=item.id, item_destino_version=item.version,
                                           tipo_relacion='HIJ').exclude(activo=False)
        for ap in padres:
            item_origen = ap.item_origen
            item_destino = ap.item_destino
            MG.add_edge(item_origen.id, item_destino.id)

    if nx.simple_cycles(MG).__len__() == 0:
        return True
    else:
        return False


@login_required
def delete_relacion(request, id_item):
    """
    Vista para modificar las relaciones de un item
    """
    context = RequestContext(request)
    item = Item.objects.get(id=id_item)
    if request.method == 'POST':
        form = delete_relacion_form(request.POST)

        if form.is_valid():
            relacion_id = request.POST.__getitem__('relacion')
            relacion = relaciones.objects.get(id=relacion_id)
            relacion.delete()
            #item = Item.objects.get(id=id_item)
            return HttpResponseRedirect('/item/listar_item/' + str(item.fase_id))
        else:
            print form.errors
    else:
        form = delete_relacion_form()
        form.fields["relacion"].queryset = relaciones.objects.filter(item_destino=id_item, item_destino_version=item.version)

    fase = item.fase
    proy = fase.proyecto
    return render_to_response('delete_relacion.html', {'form': form, 'id_item': id_item, 'nombre_item': item.nombre,
                                                       'id_fase': fase.id, 'nombre_fase': fase.nombre,
                                                       'id_proyecto': proy.id, 'proy_nombre': proy.nombre}, context)


@login_required()
def activar_item(request, id_item):
    """
    Vista para activar item, se muestra si el item esta en estado revision o aprobado
    """
    context = RequestContext(request)
    item = Item.objects.get(id=id_item)
    proyecto = item.fase.proyecto
    users = User.objects.filter(groups__permissions=Permission.objects.get(codename='activar_item'))
    if es_miembro(request.user.id, proyecto.id) and request.user in users:
        item.estado = 'ACT'
        item.save()
    else:
        #error: no tiene permisos o no es miembro
        mensaje = 'Usted no es miembro del proyecto, o no tiene permisos'
        return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)
    return HttpResponseRedirect('/item/listar_item/' + str(item.fase.id)+"/")


@login_required()
def aprobar_item(request, id_item):
    """
    Vista para aprobar el item, se muestra si el item esta en estado revision
    """
    context = RequestContext(request)
    item = Item.objects.get(id=id_item)
    proyecto = item.fase.proyecto
    users = User.objects.filter(groups__permissions=Permission.objects.get(codename='aprobar_item'))
    print es_miembro(request.user.id, proyecto.id)
    print request.user in users
    if es_miembro(request.user.id, proyecto.id) and request.user in users:
        item.estado = "APROB"
        item.save()
    else:
        #error: no tiene permisos o no es miembro
        mensaje = 'Usted no es miembro del proyecto, o no tiene permisos'
        return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)
    return HttpResponseRedirect('/item/listar_item/' + str(item.fase.id)+"/")


def es_miembro(id_user, id_proyecto):
    p = Proyecto.objects.get(id=id_proyecto)
    miembros = p.miembros.filter(id=id_user)
    if miembros.__len__() == 0:
        return False
    else:
        return True