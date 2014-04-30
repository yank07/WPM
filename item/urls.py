from django.conf.urls import patterns, url
from item import views


urlpatterns = patterns('',
    #crear vista que liste los items de la fase cuyo id se recibe
    url(r'^listar_item/(\d+)/$', views.listar_item, name='listar_item'),
    url(r'^add_item/(\d+)/$', views.add_item, name='add_item'),
    url(r'^asignar_valor_item/(\d+)/$', views.asignar_valor_item, name='asignar_valor_item'),
)