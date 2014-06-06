"""
Creado el 1 abril  2014
@author: Grupo 04
"""
import os
from django import forms
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.query import QuerySet

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from WPM.settings import RUTA_PROYECTO
from item.models import Item, relaciones
from proyecto.forms import ProyectoForm , ProyectoFilter, FaseForm
from principal.forms import UserForm, UserProfileForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User, Group
# Create your views here.
#from principal.models import Rol
from proyecto.models import Proyecto, Fase
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig, Table
from proyecto.tables import ProyectoTable , FasesTable, ListaItemTable
from django.views.generic.edit import UpdateView
from django.forms.util import ErrorList
from proyecto.forms import *
from TipoItemApp.models import TipoItem

import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# Create your views here.


@login_required
@staff_member_required
def admin_proyecto(request):
    """
    Renderiza la pagina de proyectos
    @param request: Peticion HTTP
    @return: el form correspondiente
    """
    #lista = Proyecto.objects.all()
    f = ProyectoFilter(request.GET, queryset=Proyecto.objects.all())

    lista = ProyectoTable(f)

    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('admin_proyectos.html', {'lista': lista , 'filter': f}, context_instance=RequestContext(request))


@login_required
@staff_member_required
def add_proyecto(request):
    """
    Vista para agregar un proyecto.
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    # Obtener el contexto del request.
    context = RequestContext(request)
    # es POST?
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        # el form es valido?
        if form.is_valid():
            # guardar
            p = form.save()
            p.usuario_modificacion = request.user
            p.save()
            return HttpResponseRedirect('/admin_proyectos')
        else:
            # hubo errores
            print form.errors
    else:
        # si no fue un post, mostrar el form
        form = ProyectoForm()
    return render_to_response('add_proyecto.html', {'form': form}, context)


@login_required
def proyecto_detail(request, id):
    """Metodo de para Editar un Proyecto en Particular
    """
    proyecto = Proyecto.objects.get(pk=int(id))

    if request.method == 'POST':
        form = ProyectoForm(request.POST,instance=proyecto)
    # el form es valido?
        if form.is_valid():
            # guardar
            estado = form.cleaned_data['estado']
            num_fases = form.cleaned_data['numero_fases']
            print "estado " + estado
            print "numero de fases  " + str(num_fases)
            print "proyecto numero de fases viejo" + str(Proyecto.objects.get(pk=int(id)).numero_fases)
            if Proyecto.objects.get(pk=int(id)).numero_fases != num_fases:
                print "cambio numero de fases"
                if proyecto.estado != "Pendiente":
                    error = "No se puede editar las fases de un Proyecto en estado distinto a Pendiente"

                    errors = form._errors.setdefault("numero_fases", ErrorList())
                    errors.append(error)
                    return render_to_response('edit_proyecto1.html', {'form': form ,'id':proyecto.id,
                                                                      'proy_nombre':proyecto.nombre},
                                              context_instance=RequestContext(request))
            f=form.save()
            f.usuario_modificacion = request.user
            f.save()
            return HttpResponseRedirect('/admin_proyectos')
        else:
            # hubo errores
            print form.errors
    else:
        form = ProyectoForm(instance=proyecto)
        return render_to_response('edit_proyecto1.html', {'form': form ,'id':proyecto.id,
                                                          'proy_nombre':proyecto.nombre},
                                  context_instance=RequestContext(request))


@login_required
class ProyectoUpdate(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'edit_proyecto.html'
    success_url = '/admin_proyectos/'


@login_required
@staff_member_required
def delete_proyecto(request,id):
    """
    funcion para eliminar un proyecto
    """
    server = get_object_or_404(Proyecto, pk=id)
    if request.method=='POST':
        server.delete()
        return HttpResponseRedirect('/admin_proyectos')


@login_required
def proyecto_view(request,id_proyecto):
    """

    Lista las fases de un proyecto

    """
    # pry = Proyecto.objects.get(id=id_proyecto)
    # if request.user not in pry.miembros:
    #     #pagina de error
    #     msg = 'No es miembro de este proyecto'
    #     return render_to_response('template', {'mensaje': msg}, context_instance=RequestContext(request))
    fases = Fase.objects.filter(proyecto= id_proyecto)


    lista = FasesTable(fases)
    nombre = Proyecto.objects.get(id=id_proyecto).nombre
    proyecto = Proyecto.objects.get(id=id_proyecto)

    finalizado = True
    for fase in fases:
        if fase.estado != "Finalizado":
            finalizado = False



    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('proyecto_view.html', {'lista': lista, 'proy_nombre': nombre, 'id_proyecto': id_proyecto ,'finalizado': finalizado , "proyecto":proyecto},
                              context_instance=RequestContext(request))


@login_required
def fase_detail(request,id):
    """Metodo de para Editar una Fase en Particular

    """
    fase = Fase.objects.get(pk=int(id))
    proyecto = fase.proyecto

    if request.method == 'POST':
        form = FaseForm(request.POST,instance=fase)
    # el form es valido?
        if form.is_valid():
            # guardar
            f = form.save(commit=False)
            f.usuario_modificacion = request.user
            f.save()
            return HttpResponseRedirect('/proyecto_view/'+ str(proyecto.id)+"/")
        else:
            # hubo errores
            print form.errors
    else:
        form = FaseForm(instance=fase)
        return render_to_response('edit_fase.html', {'form': form ,'id':fase.id}, context_instance=RequestContext(request))


@login_required
def delete_fase(request,id):
    """
    funcion para eliminar una Fase
    """
    fase = get_object_or_404(Fase, pk=id)
    proyecto = fase.proyecto
    proyecto.numero_fases= proyecto.numero_fases -1
    proyecto.save()

    if request.method=='POST':
        #Controlar si el Proyecto esta activo
        fase.delete()
        return HttpResponseRedirect('/proyecto_view/'+ str(proyecto.id)+"/")



@login_required
def importar_fase(request,fase_id):
    """
    Vista para importar un tipo de item a una fase
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    context = RequestContext(request)
    if request.method == 'POST':
        form = importar_fase_form(request.POST)
        if form.is_valid():
            faseID = request.POST.__getitem__('fase')
            fase = Fase.objects.get(id=faseID)

            fase2 = Fase.objects.get(id=fase_id)

            ti=TipoItem.objects.filter(fases__id=fase.id)
            n=0
            for t in ti:

                print ti[n].fases.add(fase2)
                n=n+1


            #tipoitem.fases.add(fase)
            return HttpResponseRedirect('/admin_proyectos/')
        else:
            print form.errors
    else:
        form = importar_fase_form()
    return render_to_response('importar_fase.html', {'form': form}, context)



@login_required
def finalizar_fase(request, fase_id):
    """
    Vista para finalizar una fase
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    if request.method == 'POST':
        fase = Fase.objects.get(id=fase_id)
        if request.user == fase.proyecto.usuario:

            if Item.objects.filter(fase_id=fase_id, estado="REV" ).exists() or Item.objects.filter(fase_id=fase_id, estado="ACT" ).exists() or Item.objects.filter(fase_id=fase_id, estado="APROB" ).exists():
                context = RequestContext(request)
                mensaje = 'Existe algun item no bloqueado'
                return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)

            fase.estado = "Finalizado"
            fase.save()
        else:
            context = RequestContext(request)
            mensaje = 'Usted no es el lider del proyecto, no puede finalizar una fase'
            return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)
    return HttpResponseRedirect('/item/listar_item/'+ str(fase_id)+"/")


@login_required
def finalizar_proyecto(request, proyecto_id):
    """
    Vista para finalizar un Proyecto
    @param request: Peticion HTTP
    @return renderiza el form correspondiente
    """
    if request.method == 'POST':
        proyecto = Proyecto.objects.get(id=proyecto_id)
        if request.user == proyecto.usuario:
            proyecto.estado = "Finalizado"
            proyecto.save()
        else:
            context = RequestContext(request)
            mensaje = 'Usted no es el lider del proyecto, no puede finalizar una fase'
            return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)
    return HttpResponseRedirect('/proyecto_view/21/'+ str(proyecto_id)+"/")



@login_required
def ver_grafo_relaciones(request, id_proyecto):
    """
    Vista para crear el grafo de relaciones entre items de un proyecto dado
    """
    context = RequestContext(request)
    fases = Fase.objects.filter(proyecto=id_proyecto)
    MG = nx.MultiDiGraph()

    #crear nodos
    i = 0

    x = 0
    labels = {}
    for fase in fases:
        items = Item.objects.filter(fase_id=fase.id).exclude(estado='ELIM')
        print items
        i = i + 1
        for item in items:
            x = x + 1
            labels[item.id] = item.id
            MG.add_node(item.id, pos=(item.id, x))

    color_list = []
    for node in nx.nodes(MG):
        item = Item.objects.get(id=node)
        color_list.append(item.fase_id)
    pos = nx.get_node_attributes(MG, 'pos')
    pos = nx.circular_layout(MG)
    nx.draw_networkx_nodes(MG, pos=pos, node_color=color_list, node_size=1500)
    nx.draw_networkx_labels(MG, pos=pos, labels=labels)

    #crear arcos
    edge_labels = []
    for fase in fases:
        items = Item.objects.filter(fase_id=fase.id).exclude(estado='ELIM')
        for item in items:
            antecesores_padres = relaciones.objects.filter(item_destino_id=item.id, item_destino_version=item.version).exclude(activo=False)
            for ap in antecesores_padres:
                item_origen = ap.item_origen
                item_destino = ap.item_destino
                edge = MG.add_edge(item_origen.id, item_destino.id)
                edge_labels.append(((item_origen.id, item_destino.id), ap.tipo_relacion))
    #endfor
    nx.draw_networkx_edges(MG, pos=pos)

    #agregar etiquetas a los arcos
    edge_labels = dict(edge_labels)
    nx.draw_networkx_edge_labels(MG, pos=pos, edge_labels=edge_labels)

    image_path = os.path.join(RUTA_PROYECTO,"static/grafos/image.png")
    print image_path
    #verificar que no existan conflictos de nombres
    plt.savefig(image_path)
    #plt.show()

    itemlist = []
    for fase in fases:
        items = Item.objects.filter(fase_id=fase.id)
        for item in items:
            itemlist.append(item)

    items = Item.objects.filter(fase__proyecto_id=id_proyecto)
    itemlist = ListaItemTable(items)
    proy = Proyecto.objects.get(id=id_proyecto)
    RequestConfig(request, paginate={"per_page": 5}).configure(itemlist)
    return render_to_response('ver_grafo_relaciones.html', {'image_name': "image.png", 'lista': itemlist,
                                                            'id_proyecto': id_proyecto, 'proyecto': proy},
                              context)

def get_items(id_item, version, lista=[]):
    item = Item.objects.get(id=id_item)
    sucesores_hijos = relaciones.objects.filter(item_origen_id=id_item, item_origen_version=version).exclude(activo=False)
    for sh in sucesores_hijos:
        lista.append(sh.item_destino)
        get_items(sh.item_destino_id, sh.item_destino_version,lista)




@login_required
def ver_grafo_desde_item(request, id_item):
    """
    Vista para crear el grafo de relaciones entre items de un proyecto dado
    """
    context = RequestContext(request)
    MG = nx.MultiDiGraph()
    item = Item.objects.get(id=id_item)
    print item
    lista_items=[item]
    get_items(id_item,item.version,lista_items)
    lista_items = list(set(lista_items))
    print lista_items
    #crear nodos
    i = 0

    x = 0
    labels = {}
    for item in lista_items:
        x = x + 1
        labels[item.id] = item.id
        MG.add_node(item.id, pos=(item.id, x))

    color_list = []
    for node in nx.nodes(MG):
        item = Item.objects.get(id=node)
        color_list.append(item.fase_id)
    pos = nx.get_node_attributes(MG, 'pos')
    #pos = nx.circular_layout(MG)
    nx.draw_networkx_nodes(MG, pos=pos, node_color=color_list, node_size=1500)
    nx.draw_networkx_labels(MG, pos=pos, labels=labels)

    #crear arcos
    edge_labels = []
    for item in lista_items:
        antecesores_padres = relaciones.objects.filter(item_origen_id=item.id, item_origen_version=item.version).exclude(activo=False)
        for ap in antecesores_padres:
            item_origen = ap.item_origen
            item_destino = ap.item_destino
            edge = MG.add_edge(item_origen.id, item_destino.id)
            edge_labels.append(((item_origen.id, item_destino.id), ap.tipo_relacion))
    #endfor
    print pos
    print edge_labels
    nx.draw_networkx_edges(MG, pos=pos)

    #agregar etiquetas a los arcos
    edge_labels = dict(edge_labels)
    nx.draw_networkx_edge_labels(MG, pos=pos, edge_labels=edge_labels)

    image_path = os.path.join(RUTA_PROYECTO,"static/grafos/image.png")
    #verificar que no existan conflictos de nombres
    plt.savefig(image_path)
    #plt.show()

    item_orig = Item.objects.get(id=id_item)
    itemlist = ListaItemTable(lista_items)
    RequestConfig(request, paginate={"per_page": 5}).configure(itemlist)
    return render_to_response('ver_grafo_desde_item.html', {'image_name': "image.png", 'lista': itemlist,
                                                            'item': item_orig} , context)
