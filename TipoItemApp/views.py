from django.forms.util import ErrorList
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import UpdateView
import eav
from eav.models import Attribute, Entity
from eav.registry import Registry
from TipoItemApp.forms import add_tipoitem_form, add_atributo_form, listar_atributos_form, delete_tipoitem_form, \
    delete_atributo_form, edit_atributo_form, importar_tipooitem_form
from TipoItemApp.models import TipoItem
from proyecto.models import Fase


def admin_tipoitem(request):
    """
    Vista para administrar tipos de item.
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    return render_to_response('admin_tipoitem.html',{"TipoItemList": TipoItem.objects.all()},
                              context_instance=RequestContext(request))

def listar_atributos(request):
    """
    Vista para listar atributos.
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    context = RequestContext(request)
    if request.method == 'POST':
        form = listar_atributos_form(request.POST)
        if form.is_valid():
            tipoitemID = request.POST.__getitem__('nombre')
            tipoitem = TipoItem.objects.get(id=tipoitemID)
            form = listar_atributos_form()
            return render_to_response('listar_atributos.html',{'form': form,'AttrList': tipoitem.atributos.all()},
                                      context)
        else:
            print form.errors
    else:
        attr_list = Attribute.objects.all()
        form = listar_atributos_form()
    return render_to_response('listar_atributos.html', {'form': form,'AttrList':attr_list}, context)

def add_tipoitem(request):
    """
    Vista para agregar un tipo de item.
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
 # Obtener el contexto del request.
    context = RequestContext(request)
    # es POST?
    if request.method == 'POST':
        form = add_tipoitem_form(request.POST)
        # el form es valido?
        if form.is_valid():
            fasesidlist=request.POST.getlist('fases')
            print fasesidlist
            for faseid1 in fasesidlist:
                fase1 = Fase.objects.get(id=faseid1)
                p1=fase1.proyecto
                for faseid2 in fasesidlist:
                    fase2 = Fase.objects.get(id=faseid2)
                    p2=fase2.proyecto
                    if p1 != p2:
                        errors=form._errors.setdefault("fases",ErrorList())
                        errors.append("Elegir fases del mismo proyecto")
                        return render_to_response('add_tipoitem.html', {'form': form}, context)

            form.save(commit=True)
            return admin_tipoitem(request)
        else:
            # hubo errores
            print form.errors
    else:
        # si no fue un post, mostrar el form
        form = add_tipoitem_form()
    return render_to_response('add_tipoitem.html', {'form': form}, context)

def add_atributo(request):
    """
    Vista para agregar un atributo
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    #solo ejecutar esta vista si proyecto.estado = ACTIVO
    context = RequestContext(request)
    if request.method == 'POST':
        form = add_atributo_form(request.POST)
        if form.is_valid():
            nombre = request.POST.__getitem__('nombre_atributo')
            tipo = request.POST.__getitem__('tipo')
            obligatorio = 'off'
            if request.POST.__contains__('obligatorio'):
                obligatorio = request.POST.__getitem__('obligatorio')
            valor = False
            if obligatorio == 'on':
                valor = True
            if request.POST.__getitem__('tipo_item') != '':
                tipoitemID = request.POST.__getitem__('tipo_item')
                print tipoitemID
                tipoitem = TipoItem.objects.get(id=tipoitemID)
                a1 = Attribute.objects.create(name=nombre, datatype=tipo,required=valor,type=tipoitemID)
                a1.save()
                tipoitem.atributos.add(a1)
            else:
                a1 = Attribute.objects.create(name=nombre, datatype=tipo,required=valor)
                a1.save()
            return admin_tipoitem(request)
        else:
            print form.errors
    else:
        form = add_atributo_form()
    return render_to_response('add_atributo.html', {'form': form}, context)


def edit_tipoitem(request, tipoitem_id):
    """
    Vista para agregar un tipo de item.
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    #solo ejecutar esta vista si proyecto.estado = pendiente
    tipoitem = TipoItem.objects.get(id=tipoitem_id)
    context = RequestContext(request)
    if request.method == 'POST':
        form = add_tipoitem_form(request.POST,instance=tipoitem)
        sw=False
        if form.is_valid():
            fasesidlist=request.POST.getlist('fases')
            print fasesidlist
            for faseid1 in fasesidlist:
                fase1 = Fase.objects.get(id=faseid1)
                p1=fase1.proyecto
                for faseid2 in fasesidlist:
                    fase2 = Fase.objects.get(id=faseid2)
                    p2=fase2.proyecto
                    if p1 != p2:
                        errors=form._errors.setdefault("fases",ErrorList())
                        errors.append("Elegir fases del mismo proyecto")
                        return render_to_response('edit_tipoitem.html', {'form': form,'tipoitem_id':tipoitem_id}, context)
            fase1 = Fase.objects.get(id=fasesidlist[0])
            p1=fase1.proyecto.estado
            if p1 != 'Pendiente':
                errors=form._errors.setdefault("fases",ErrorList())
                errors.append("No se puede modificar un tipo de item de un proyecto en estado activo")
                return render_to_response('edit_tipoitem.html', {'form': form,'tipoitem_id':tipoitem_id}, context)
            form.save(commit=True)
            return HttpResponseRedirect('/admin_tipoitem/')
        else:
            print form.errors
    else:
        form = add_tipoitem_form(instance=tipoitem)
    return render_to_response('edit_tipoitem.html', {'form': form,'tipoitem_id':tipoitem_id}, context)


def edit_atributo(request, atributo_id):
    """
    Vista para agregar un tipo de item.
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    #solo ejecutar esta vista si proyecto.estado = pendiente
    attr = Attribute.objects.get(id=atributo_id)
    context = RequestContext(request)
    if request.method == 'POST':
        form = edit_atributo_form(request.POST)
        if form.is_valid():
            nombre = request.POST.__getitem__('nombre')
            tipo = request.POST.__getitem__('tipo')
            obligatorio = request.POST.__contains__('obligatorio')
            attr.datatype=tipo
            attr.name=nombre
            attr.required=obligatorio
            attr.save()
            return admin_tipoitem(request)
        else:
            print form.errors
    else:
        form = edit_atributo_form(initial={'tipo':attr.datatype,
                                          'nombre':attr.name,
                                          'obligatorio':attr.required})
    return render_to_response('edit_atributo.html', {'form': form,'atributo_id':atributo_id}, context)


def delete_tipoitem(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = delete_tipoitem_form(request.POST)
        if form.is_valid():
            tipoitemID = request.POST.__getitem__('nombre')
            tipoitem = TipoItem.objects.get(id=tipoitemID)
            tipoitem.delete()
            return admin_tipoitem(request)
        else:
            print form.errors
    else:
        form = delete_tipoitem_form()
    return render_to_response('delete_tipoitem.html', {'form': form}, context)

def delete_atributo(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = delete_atributo_form(request.POST)
        if form.is_valid():
            attrID = request.POST.__getitem__('nombre')
            attr = Attribute.objects.get(id=attrID)
            attr.delete()
            return admin_tipoitem(request)
        else:
            print form.errors
    else:
        form = delete_atributo_form()
    return render_to_response('delete_atributo.html', {'form': form}, context)

def importar_tipoitem(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = importar_tipooitem_form(request.POST)
        if form.is_valid():
            tipoitemID = request.POST.__getitem__('tipoitem')
            tipoitem = TipoItem.objects.get(id=tipoitemID)
            faseID = request.POST.__getitem__('fase')
            fase = Fase.objects.get(id=faseID)
            tipoitem.fases.add(fase)
            return admin_tipoitem(request)
        else:
            print form.errors
    else:
        form = importar_tipooitem_form()
    return render_to_response('importar_tipoitem.html', {'form': form}, context)