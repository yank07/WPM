from django.conf.urls import patterns, url
from item import views


urlpatterns = patterns('',
    #crear vista que liste los items de la fase cuyo id se recibe
    url(r'^(\d+)/$', views.add_item, name='index'),
    url(r'^add_item/$', views.add_item, name='add_item'),
    url(r'^asignar_valor_item/$', views.asignar_valor_item, name='asignar_valor_item'),
)