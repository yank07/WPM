__author__ = 'ccaballero'

from django.conf.urls import patterns, url
from solicitudCambio import views

urlpatterns = patterns('',
                       url(r'^listar/$', views.listar_solicitudes, name='listar_solicitudes'),
                       url(r'^crear/(\d+)/$', views.crear_solicitud, name='crear_solicitud'),
                       url(r'^rechazar/(\d+)/$', views.rechazar_solicitud, name='rechazar_solicitud'),
                       url(r'^aprobar/(\d+)/$', views.aprobar_solicitud, name='aprobar_solicitud'),
                       url(r'^eliminar/(\d+)/$', views.eliminar_solicitud, name='eliminar_solicitud'),
                       url(r'^crear_comite/(\d+)/$', views.crear_comite, name='crea_comite'),
                       url(r'^admin_comite/$', views.admin_comite, name='admin_comite'),
                       url(r'^editar_comite/(\d+)/$', views.editar_comite, name='editar_comite'),
                       url(r'^voto_favor/(\d+)/$', views.voto_positivo, name='voto_favor'),
                       url(r'^voto_contra/(\d+)/$', views.voto_negativo, name='editar_comite'),




                       )