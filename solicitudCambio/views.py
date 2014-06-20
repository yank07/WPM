from django import forms
from django.contrib.auth.decorators import login_required
from django.forms.util import ErrorList
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django_tables2 import RequestConfig
from lineaBase.models import LineaBase
from proyecto.views import ver_grafo_desde_item
from solicitudCambio.models import Solicitud, Comite
from solicitudCambio.forms import CrearSolicitudForm, SolicitudFilter, crear_comite_form, comite_filter
from item.models import Item, relaciones
from item.views import calculo_impacto
from proyecto.models import Proyecto, Fase
from solicitudCambio.tables import SolicitudTable, admin_comite_table, MisSolicitudesTable
from item.views import es_miembro
from django.db.models import Q


@login_required()
def listar_mis_solicitudes(request):
    """
    Vista para listar las solicitudes de cambio que pertenecen a un usuario particular
    """
    f = SolicitudFilter(request.GET, queryset=Solicitud.objects.filter(usuario=request.user))
    tabla = MisSolicitudesTable(f)
    RequestConfig(request, paginate={"per_page": 5}).configure(tabla)

    return render_to_response('mis_solicitudes.html', {'lista': tabla, 'filter': f},
                              context_instance=RequestContext(request))


@login_required()
def listar_solicitudes(request):
    """
    Vista para listar las solicitudes de cambio. Se listan solo las solicitudes
    de proyectos donde el usuario es miembro
    """

    comites = Comite.objects.filter(Q(primer_integrante=request.user) | Q(segundo_integrante=request.user) |
                                    Q(tercer_integrante=request.user))

    proyectos = []
    for c in comites:
        proyectos.append(c.proyecto)

    f = SolicitudFilter(request.GET, queryset=Solicitud.objects.filter(item=Item.objects.filter(
        fase=Fase.objects.filter(proyecto__in=proyectos))))

    tabla = SolicitudTable(f)
    RequestConfig(request, paginate={"per_page": 5}).configure(tabla)

    return render_to_response('admin_solicitud.html', {'lista': tabla, 'filter': f},
                              context_instance=RequestContext(request))


@login_required
def crear_solicitud(request, item_id):
    """
    Vista para crear la solicitud
    """
    context = RequestContext(request)
    item = Item.objects.get(id=item_id)
    form = CrearSolicitudForm()
    if es_miembro(request.user.id, item.fase.proyecto.id):
        if request.method == 'POST':
            form = CrearSolicitudForm(request.POST)
            if form.is_valid():
                sc = form.save(commit=False)
                sc.item = item
                sc.estado = 'PEN'
                sc.impacto = calculo_impacto(item.id)
                sc.usuario = request.user
                sc.save()
                url = reverse('item.views.listar_item', args=[item.fase.id])
                return HttpResponseRedirect(url)
            else:
                print form.errors
    else:
        #error: no tiene permisos o no es miembro
        mensaje = 'Usted no es miembro del proyecto, o no tiene permisos'
        return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)
    return render_to_response('crear.html', {'form': form, 'nombre_item': item.nombre,
                                             'id_fase': item.fase.id, 'nombre_fase': item.fase.nombre,
                                             'id_proyecto': item.fase.proyecto.id,
                                             'proy_nombre': item.fase.proyecto.nombre}, context)


@login_required()
def rechazar_solicitud(request, id_solicitud):
    """
    Vista para rechazar una solicitud.
    """
    context = RequestContext(request)
    sc = Solicitud.objects.get(id=id_solicitud)
    if es_miembro(request.user.id, sc.item.fase.proyecto.id):
        sc.estado = 'DEN'
        sc.save()
        url = reverse('solicitudCambio.views.listar_solicitudes')
        return HttpResponseRedirect(url)
    else:
        #error: no tiene permisos o no es miembro
        mensaje = 'Usted no es miembro del proyecto, o no tiene permisos'
        return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)


@login_required()
def aprobar_solicitud(request, id_solicitud):
    """
    Vista para aprobar la solicitud. Pone el item en cuestion y sus descendientes/sucesores
    a Revision, y las lineas base implicadas a Abierta
    """
    context = RequestContext(request)
    sc = Solicitud.objects.get(id=id_solicitud)
    if es_miembro(request.user.id, sc.item.fase.proyecto.id):
        sc.estado = 'APR'
        sc.save()
        activar_items(sc.item.id)
        url = reverse('solicitudCambio.views.listar_solicitudes')
        return HttpResponseRedirect(url)
    else:
        #error: no tiene permisos o no es miembro
        mensaje = 'Usted no es miembro del proyecto, o no tiene permisos'
        return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)


@login_required()
def voto_positivo(request, id_solicitud):
    """
    Vista para votar a favor de una solicitud
    """
    context = RequestContext(request)
    sc = Solicitud.objects.get(id=id_solicitud)
    comite = Comite.objects.get(proyecto=sc.item.fase.proyecto)

    if comite.primer_integrante == request.user:
        if sc.voto_primero == 0:
            sc.voto_primero = 1
        else:
            #error
            mensaje = 'Usted ya ha votado'
            return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)

    if comite.segundo_integrante == request.user:
        if sc.voto_segundo == 0:
            sc.voto_segundo = 1
        else:
            #error
            mensaje = 'Usted ya ha votado'
            return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)

    if comite.tercer_integrante == request.user:
        if sc.voto_tercero == 0:
            sc.voto_tercero = 1
        else:
            #error
            mensaje = 'Usted ya ha votado'
            return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)
    sc.conteo += 1
    if sc.conteo == 3:
        sc.resultado = sc.voto_primero + sc.voto_segundo + sc.voto_tercero
    sc.save()
    url = reverse('solicitudCambio.views.listar_solicitudes')
    #return HttpResponseRedirect(url)
    return render_to_response('voto.html', {'voto': True}, context)


@login_required()
def voto_negativo(request, id_solicitud):
    """
    Vista para votar en contra de una solicitud
    """
    context = RequestContext(request)
    sc = Solicitud.objects.get(id=id_solicitud)

    comite = Comite.objects.get(proyecto=sc.item.fase.proyecto)

    if comite.primer_integrante == request.user:
        if sc.voto_primero == 0:
            sc.voto_primero = -1
        else:
            #error
            mensaje = 'Usted ya ha votado'
            return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)

    if comite.segundo_integrante == request.user:
        if sc.voto_segundo == 0:
            sc.voto_segundo = -1
        else:
            #error
            mensaje = 'Usted ya ha votado'
            return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)

    if comite.tercer_integrante == request.user:
        if sc.voto_tercero == 0:
            sc.voto_tercero = -1
        else:
            #error
            mensaje = 'Usted ya ha votado'
            return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)
    sc.conteo += 1
    if sc.conteo == 3:
        sc.resultado = sc.voto_primero + sc.voto_segundo + sc.voto_tercero
    sc.save()

    url = reverse('solicitudCambio.views.listar_solicitudes')
    #return HttpResponseRedirect(url)
    return render_to_response('voto.html', {'voto': False}, context)


@login_required()
def eliminar_solicitud(request, id_solicitud):
    """
    Vista para eliminar la solicitud, DEBE estar en estado pendiente
    """
    context = RequestContext(request)
    sc = Solicitud.objects.get(id=id_solicitud)
    if sc.estado == 'PEN':
        sc.delete()
    else:
        mensaje = 'No se pudo eliminar la solicitud, Esta debe estar en estado PENDIENTE'
        return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)
    url = reverse('solicitudCambio.views.listar_solicitudes')
    return HttpResponseRedirect(url)


@login_required
def crear_comite(request, id_proyecto):
    """
    Vista para crear un comite
    """
    context=RequestContext(request)
    proyecto = Proyecto.objects.get(pk=int(id_proyecto))
    lider=proyecto.usuario
    if request.user != lider:
        mensaje = 'Usted no es lider del proyecto, no puede crear un comite'
        return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)

    if request.method == 'POST':
        form = crear_comite_form(request.POST)
        if form.is_valid():
            primer_integrante=form.cleaned_data['primer_integrante']
            segundo_integrante=form.cleaned_data['segundo_integrante']
            tercer_integrante=form.cleaned_data['tercer_integrante']
            print form.cleaned_data['proyecto']
            form.cleaned_data['proyecto'] = proyecto
            print form.cleaned_data['proyecto']
            if primer_integrante == segundo_integrante or primer_integrante == tercer_integrante or \
                segundo_integrante == tercer_integrante:
                error = "Los miebros del comite deben ser usuarios distintos"
                errors = form._errors.setdefault("primer_integrante", ErrorList())
                errors.append(error)
                form.fields['proyecto'].widget = forms.HiddenInput()
                return render_to_response('crear_comite.html', {'form': form, 'id_proyecto': id_proyecto}, context)

            form.save()
            return HttpResponseRedirect('/')
        else:
            form.fields['proyecto'].widget = forms.HiddenInput()
            print form.errors
    else:
        form = crear_comite_form(initial={'proyecto':proyecto})
        form.fields['proyecto'].widget = forms.HiddenInput()
    return render_to_response('crear_comite.html', {'form': form ,'id_proyecto':proyecto.id},
                                  context_instance=context)


@login_required
def admin_comite(request):
    """
    Vista para la administracion de los comites
    """
    #lista = Proyecto.objects.all()
    f = comite_filter(request.GET, queryset=Comite.objects.all())
    lista = admin_comite_table(f)

    RequestConfig(request, paginate={"per_page": 5}).configure(lista)
    return render_to_response('admin_comite.html', {'lista': lista, 'filter': f},
                              context_instance=RequestContext(request))


@login_required
def editar_comite(request, id_comite):
    """
    Vista para crear un comite
    """
    context=RequestContext(request)
    comite=Comite.objects.get(id=id_comite)
    proyecto = Proyecto.objects.get(pk=int(comite.proyecto_id))
    lider=proyecto.usuario
    if request.user != lider:
        mensaje = 'Usted no es lider del proyecto, no puede editar este comite'
        return render_to_response('pagina_error.html', {'mensaje': mensaje}, context)

    if request.method == 'POST':
        form = crear_comite_form(request.POST)
        # id=comite.id
        # comite_nuevo=comite
        # comite.delete()
        if form.is_valid():
            primer_integrante=form.cleaned_data['primer_integrante']
            segundo_integrante=form.cleaned_data['segundo_integrante']
            tercer_integrante=form.cleaned_data['tercer_integrante']
            estado=form.cleaned_data['estado']
            if primer_integrante == segundo_integrante or primer_integrante == tercer_integrante or \
                segundo_integrante == tercer_integrante:
                print 'AAAAAAAAAAAAAAAAAAAAAAAA'
                error = "Los miebros del comite deben ser usuarios distintos"
                errors = form._errors.setdefault("primer_integrante", ErrorList())
                errors.append(error)
                form.fields['proyecto'].widget = forms.HiddenInput()
                return render_to_response('editar_comite.html', {'form': form, 'id_comite': id_comite}, context)

            # comite_nuevo.proyecto=proyecto
            # comite_nuevo.primer_integrante=primer_integrante
            # comite_nuevo.segundo_integrante=segundo_integrante
            # comite_nuevo.tercer_integrante=tercer_integrante
            # comite_nuevo.estado=estado
            # comite_nuevo.id=id
            # comite_nuevo.save()
            comite.primer_integrante=primer_integrante
            comite.segundo_integrante=segundo_integrante
            comite.tercer_integrante=tercer_integrante
            comite.estado = estado
            comite.save()
            url = reverse('solicitudCambio.views.admin_comite')
            return HttpResponseRedirect(url)
        else:
            print form.errors
    else:
        diccionario= {'proyecto': proyecto, 'primer_integrante': comite.primer_integrante,
                     'segundo_integrante': comite.segundo_integrante,
                     'tercer_integrante': comite.tercer_integrante, 'estado': comite.estado}
        form = crear_comite_form(initial=diccionario)
        form.fields['proyecto'].widget = forms.HiddenInput()
        #form.fields['estado'].widget = forms.HiddenInput()
    return render_to_response('editar_comite.html', {'form': form, 'id_comite': comite.id},
                                  context_instance=context)


def activar_items(id_item):
    """
    Funcion para activar los items relacionados al item de la solicitud de cambio
    """
    item = Item.objects.get(id=id_item)
    item.estado = 'REV'
    item.save()
    item.history.get(history_id=[h.history_id for h in item.history.all()][1]).delete()

    lb_list = item.linea_base.all()
    for lb in lb_list:
        lb.estado = 'ABIERTA'
        lb.save()
    sucesores_hijos = relaciones.objects.filter(item_origen_id=id_item)
    for sh in sucesores_hijos:
        activar_items(sh.item_destino.id)


@login_required()
def ver_grafo_solicitud(request, id_solicitud):
    """
    Vista que implementa el grafo de dependencias de un item, para la evaluacion de una solicitud de cambio
    """

    item = Solicitud.objects.get(id=id_solicitud).item
    return ver_grafo_desde_item(request, item.id)