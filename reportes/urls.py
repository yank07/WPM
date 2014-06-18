__author__ = 'ccaballero'
from django.conf.urls import patterns, url
from reportes import views

urlpatterns = patterns('',
                       url(r'^reporte_resumen/(\d+)/$', views.reporte_resumen_proyecto, name='reporte_resumen'),
                       url(r'^reporte_fase/(\d+)/$', views.reporte_fases, name='reporte_fases'),
                       url(r'^reporte_version_item/(\d+)/$', views.reporte_versiones_item, name='reporte_version_item'),
                       url(r'^reporte_lista_item/(\d+)/$', views.reporte_lista_items, name='reporte_lista_items'),




                       )