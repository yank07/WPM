from django.conf.urls import patterns, url
from lineaBase import views


urlpatterns = patterns('',
    #crear vista que liste los items de la fase cuyo id se recibe
    url(r'^crear/(\d+)/$', views.crear_lb, name='crear_lb'),
    url(r'^admin_lb/(\d+)/$', views.admin_lb, name='admin_lb'),
    url(r'^list_item/(\d+)/$', views.list_lb, name='list_lb'),
    url(r'^editar/(\d+)/$', views.edit_lb, name='edit_lb'),
    url(r'^cerrar/(\d+)/$', views.cerrar_linea_base, name='cerrar_lb'),




)