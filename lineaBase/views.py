from django.contrib.auth.decorators import login_required
from django.forms.util import ErrorList
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from forms import add_lb_form, LBFilter, edit_lb_form
from models import LineaBase
from item.models import Item, relaciones
from proyecto.models import Fase
from django.http import HttpResponse, HttpResponseRedirect
from tables import LBTable, ItemTable
from django_tables2 import RequestConfig


# Create your views here.

@login_required()
def crear_lb(request,id_fase):
    """
    Vista para crear linea base
    """
    context = RequestContext(request)
    fase = Fase.objects.get(id=id_fase)
    if request.method == 'POST':
        form = add_lb_form(request.POST)
        fase = Fase.objects.get(id=id_fase)

        if form.is_valid():
            linea_base = form.save()
            linea_base.fase = fase
            linea_base.save()
            if linea_base.items.all().__len__() == 0:
                errors=form._errors.setdefault("items",ErrorList())
                errors.append("Debe seleccionar al menos un item")
                form.fields["items"].queryset = Item.objects.filter(fase__id=id_fase, estado="APROB")
                return render_to_response('crear_lb.html', {'form': form,'id_fase':id_fase, 'nombre_fase': fase.nombre,
                                                            'id_proyecto': fase.proyecto.id,
                                                            'proy_nombre': fase.proyecto.nombre}, context)

            for item in linea_base.items.all():
                #print item.id
                if relaciones.objects.filter(item_destino_id=item.id ,tipo_relacion="HIJ").exclude(item_origen__estado ="BLOQ").exists():
                     errors=form._errors.setdefault("items",ErrorList())
                     errors.append("El padre de algun item no esta bloqueado")
                     form.fields["items"].queryset = Item.objects.filter(fase__id=id_fase, estado="APROB")

                     return render_to_response('crear_lb.html', {'form': form,'id_fase':id_fase,  'nombre_fase': fase.nombre, 'id_proyecto': fase.proyecto.id,
                                                   'proy_nombre': fase.proyecto.nombre }, context)


                item.estado = "BLOQ"

                item.save()
                item.history.get(history_id=[h.history_id for h in item.history.all()][1]).delete()

            return HttpResponseRedirect('/item/listar_item/'+ str(id_fase))
    else:
         form = add_lb_form()
         i = Item.objects.filter(fase__id=id_fase, estado="APROB")
         form.fields["items"].queryset = i

    return render_to_response('crear_lb.html', {'form': form,'id_fase':id_fase,  'nombre_fase': fase.nombre, 'id_proyecto': fase.proyecto.id,
                                                   'proy_nombre': fase.proyecto.nombre }, context)


@login_required()
def admin_lb(request,id_fase):
    """
    Vista para listar linea base
    """
    context = RequestContext(request)
    queryset = LineaBase.objects.filter(fase__id=id_fase)

    f = LBFilter(request.GET, queryset=queryset)
    lista = LBTable(f)
    fase = Fase.objects.get(id=id_fase)
    id_proyecto = fase.proyecto.id
    proy_nombre = fase.proyecto.nombre

    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('admin_lb.html', {'lista': lista , 'filter': f,'id_fase':fase.id,
                                                   'nombre_fase': fase.nombre, 'id_proyecto': id_proyecto,
                                                   'proy_nombre': proy_nombre},
                              context_instance=RequestContext(request))


@login_required()
def list_lb(request,id_lb):
    """
    Vista para listar los items de una linea base. Solo se permite listarlos.
    """
    context = RequestContext(request)
    queryset = Item.objects.filter(linea_base=id_lb)
    lb = LineaBase.objects.get(id=id_lb)
    id_fase = lb.fase.id

    lista = ItemTable(queryset)
    fase = Fase.objects.get(id=id_fase)
    id_proyecto = fase.proyecto.id
    proy_nombre = fase.proyecto.nombre

    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('listar_item.html', {'lista': lista,'id_fase':id_fase,
                                                   'nombre_fase': fase.nombre, 'id_proyecto': id_proyecto,
                                                   'proy_nombre': proy_nombre},
                              context_instance=RequestContext(request))


@login_required()
def edit_lb(request,id_lb):
    """
    Lista para editar linea base. Solo se permite editar la descripcion
    """
    context = RequestContext(request)
    lb = LineaBase.objects.get(id=id_lb)

    if request.method == 'POST':
        form = add_lb_form(request.POST, instance=lb)
        if form.is_valid():
            linea_base = form.save()
            return HttpResponseRedirect('/lineabase/admin_lb/'+ str(linea_base.fase.id))

    else:
         form = edit_lb_form(instance=lb)

    return render_to_response('edit_lb.html', {'form': form,}, context)


@login_required()
def cerrar_linea_base(request, id_lineabase):
    lb = LineaBase.objects.get(id=id_lineabase)
    items = lb.items.all()
    cerrada = True
    for item in items:
        if item.estado == 'APROB':
            item.estado = 'BLOQ'
            item.save()
            item.history.get(history_id=[h.history_id for h in item.history.all()][1]).delete()
    for item in items:
        if item.estado != 'BLOQ':
            cerrada = False
    if cerrada:
        lb.estado = 'CERRADA'
        lb.save()
    return HttpResponseRedirect('/lineabase/admin_lb/'+ str(lb.fase.id))