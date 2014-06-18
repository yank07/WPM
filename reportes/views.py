import datetime
from django.core.files.base import File
from django.contrib.auth.decorators import login_required
import os
from django.core.files.temp import NamedTemporaryFile
from django.http import HttpResponse
from django.template import RequestContext
from eav.models import Value
from WPM import settings
from item.models import Item, relaciones
from lineaBase.models import LineaBase
from proyecto.models import Proyecto, Fase
from solicitudCambio.models import Solicitud, Comite
from reportes.tables import SolicitudReporteTable, UsuariosReporteTable, FaseReporteTable, ItemReporteTable, \
    ItemVersionReporteTable
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template.loader import render_to_string

import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


@login_required
def reporte_resumen_proyecto(request, id_proyecto):
    """
    Vista que genera el resumen del proyecto
    :param request: Request HTTP
    :param id_proyecto: el id del proyecto para generar el reporte
    :return: respuesta en PDF
    """
    proyecto = Proyecto.objects.get(id=id_proyecto)
    generar_imagen_grafo_proyecto(proyecto.id)
    ruta_imagen = "/uploaded_files/tmp/"
    nombre_imagen = proyecto.nombre + ".png"
    save_image_in_field(proyecto.imagen_grafo, ruta_imagen, filename=nombre_imagen)

    proyectos = [proyecto]

    lista_sc = Solicitud.objects.filter(item=Item.objects.filter(fase=Fase.objects.filter(proyecto__in=proyectos)))
    #lista_sol = Solicitud.objects.filter(item=Item.objects.filter(fase=Fase.objects.filter(proyecto__in=proyectos)))
    #lista_sc = SolicitudReporteTable(lista_sol)

    miembros_lista = proyecto.miembros.all()
    miembros = UsuariosReporteTable(miembros_lista)

    comite_l = Comite.objects.filter(proyecto=proyecto)
    if comite_l.__len__() > 0:
        comite = Comite.objects.get(proyecto=proyecto)
        miembros_comite_lista = [comite.primer_integrante, comite.segundo_integrante, comite.tercer_integrante]
        miembros_comite = UsuariosReporteTable(miembros_comite_lista)
    else:
        miembros_comite_lista = []
        miembros_comite = UsuariosReporteTable(miembros_comite_lista)

    fases_lista = proyecto.fases.all()
    fases = FaseReporteTable(fases_lista)

    lista_items = Item.objects.filter(fase__in=fases_lista)

    lista_lb = LineaBase.objects.filter(fase__in=fases_lista)
    url_img = 'uploaded_files/tmp/' + proyecto.nombre + '.png'

    diccionario = {'proyecto': proyecto, 'comite': miembros_comite, 'miembros': miembros, 'sc': lista_sc,
                   'fases': fases, 'lista_fases': fases_lista, 'items': lista_items,
                   'lista_lb': lista_lb, 'fecha': fecha_actual_str(), 'img': url_img,
                   'pagesize': 'A4'}

    html = render_to_string('reporte_resumen_proyecto.html', diccionario, context_instance=RequestContext(request))
    return generar_pdf(html)

@login_required
def reporte_fases(request, fase_id):
    """
    Vista que genera el reporte de resumen de fase
    :param request: request HTTP
    :param fase_id: el ID de la fase
    :return: respuesta en PDF
    """

    fase = Fase.objects.get(id=fase_id)
    items = Item.objects.filter(fase=fase).exclude(estado='ELIM')
    tipos_item = fase.tipoitem.all()
    lista_items = ItemReporteTable(items)
    lista_lb = LineaBase.objects.filter(fase=fase)
    lista_valores = []

    for item in items:
        i = Item.objects.get(id=item.id, version=item.version)
        print range(i.rango_valor_inicio, i.rango_valor_final)
        valores = Value.objects.filter(id__in=range(i.rango_valor_inicio, i.rango_valor_final+1)).all()
        for v in valores:
            lista_valores.append(v)

    print lista_valores
    diccionario = {'pagesize': 'A4', 'lista_items': lista_items, 'lista_lb': lista_lb, 'proyecto': fase.proyecto,
                   'fecha': fecha_actual_str(), 'fase': fase, 'items': items, 'tipoitem': tipos_item,
                   'valores': lista_valores}

    html = render_to_string('reporte_fases.html', diccionario, context_instance=RequestContext(request))

    return generar_pdf(html)


@login_required
def reporte_versiones_item(request, id_item):

    item = Item.objects.get(id=id_item)
    historial = item.history.all()
    lista_items = ItemVersionReporteTable(historial)

    diccionario = {'lista_items': lista_items, 'fecha': fecha_actual_str(), 'historial': historial, 'item': item}

    html = render_to_string('reporte_versiones_item.html', diccionario, context_instance=RequestContext(request))
    return generar_pdf(html)


def generar_pdf(html):
    """
    Metodo interno utilizado para generar un pdf en base a un HTML y retornarlo al navegador
    :param html: el HTML a renderizar
    :return: el PDF renderizado encapsulado en una respuesta HTTP
    """

    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))


def fetch_resources(uri, rel):
    path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_ROOT, ""))
    return path


def fecha_actual_str():
    """Retorna la fecha actual en formato String"""
    fecha = datetime.datetime.now()

    fecha_str = ""
    fecha_str = fecha_str + str(fecha.day)
    fecha_str = fecha_str + "/" + str(fecha.month)
    fecha_str = fecha_str + "/" + str(fecha.year)
    fecha_str = fecha_str + " " + str(fecha.hour)
    fecha_str = fecha_str + ":" + str(fecha.minute)
    fecha_str = fecha_str + ":" + str(fecha.second)

    return fecha_str


def generar_imagen_grafo_proyecto(id_proyecto):
    """
    Metodo interno para graficar el grafo del proyecto
    :param id_proyecto: el ID del proyecto
    :return: el path de la imagen guardada
    """
    proyecto = Proyecto.objects.get(id=id_proyecto)
    fases = proyecto.fases.all()
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
            antecesores_padres = relaciones.objects.filter(item_destino_id=item.id, item_destino_version=item.version)\
                .exclude(activo=False)
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

    ruta = "uploaded_files/tmp/" + proyecto.nombre + ".png"

    image_path = os.path.join(settings.RUTA_PROYECTO, ruta)
    #verificar que no existan conflictos de nombres
    plt.savefig(image_path)
    MG.clear()
    plt.clf()
    return image_path


def save_image_in_field(modelfield, relativefile='', filename=None):
    """
    Metodo interno para guardar una imagen en el campo imagen de una instancia de modelo ya almacenada
    :param modelfield: el modelo a actualizar
    :param relativefile:
    :param filename: el nombre del archivo
    :return: el modelo actualizado
    """


    ruta = "uploaded_files/tmp/" + filename

    image_path = os.path.join(settings.RUTA_PROYECTO, ruta)
    print image_path
    r = open(image_path, 'rb')
    data = r.read()

    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(data)
    img_temp.flush()

    modelfield.save(filename, File(img_temp), save=True)


@login_required()
def reporte_lista_items(request, id_proyecto):

    proyecto = Proyecto.objects.get(id=id_proyecto)
    fases = proyecto.fases.all()
    lista_items = Item.objects.filter(fase__in=fases)
    lista_relaciones = relaciones.objects.filter(item_destino__in=lista_items).exclude(tipo_relacion='SUC')

    diccionario = {'fases': fases, 'lista_items': lista_items, 'lista_relaciones': lista_relaciones,
                   'proyecto': proyecto, 'fecha': fecha_actual_str()}

    html = render_to_string('reporte_lista_items.html', diccionario, context_instance=RequestContext(request))
    return generar_pdf(html)