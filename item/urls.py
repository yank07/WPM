from django.conf.urls import patterns, url
from item import views


urlpatterns = patterns('',
    #crear vista que liste los items de la fase cuyo id se recibe
    url(r'^listar_item/(\d+)/$', views.listar_item, name='listar_item'),
    url(r'^add_item/(\d+)/$', views.add_item, name='add_item'),
    url(r'^asignar_valor_item/(\d+)/$', views.asignar_valor_item, name='asignar_valor_item'),

    url(r'^edit_item/(\d+)/$', views.edit_item, name='edit_item'),
    url(r'^listar_item_muerto/(\d+)/$', views.listar_item_muerto, name='listar_item_muerto'),
    url(r'^revivir_item/(\d+)/$', views.revivir_item, name='revivir_item'),

    url(r'^crear_sucesor/(\d+)/$', views.crear_sucesor, name='crear_sucesor'),
    url(r'^crear_hijo/(\d+)/$', views.crear_hijo, name='crear_hijo'),

    url(r'^listar_versiones/(\d+)/$', views.listar_versiones, name='listar_versiones'),
    url(r'^revertir_item/(?P<id_item>\d+)/(?P<version>\d+)$', views.revertir_item, name='revertir_item'),

    url(r'^delete_relacion/(\d+)/$', views.delete_relacion, name='delete_relacion'),

    #url(r'^ver_grafo_relaciones/(\d+)/$', views.ver_grafo_relaciones, name='ver_grafo_relaciones'),
)