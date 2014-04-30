from django.conf.urls import patterns, include, url

from django.contrib import admin
from principal.views import admin_rol, add_rol, asignar_rol, admin_usuario, edit_rol, editar_usuario, delete_rol
from TipoItemApp.views import admin_tipoitem, add_tipoitem, add_atributo, listar_atributos, edit_tipoitem, \
    delete_tipoitem, delete_atributo, edit_atributo, importar_tipoitem


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WPM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'principal.views.ingresar', name='home'),

    url(r'^ingresar/$','principal.views.ingresar'),
    url(r'^accounts/login/$','principal.views.ingresar'),


    url(r'^home/$','principal.views.home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),


    url(r'^admin_usuarios/$', admin_usuario, name='admin_usuario'),
    url(r'^add_usuario/$', 'principal.views.nuevo_usuario'),
    url(r'^nuevo_usuario/perfil$', 'principal.views.user_profile'),
    url(r'^cerrar/$','principal.views.cerrar'),
    url(r'^usuarios/(?P<username>\w+)/$', editar_usuario, name='editar_usuario'),

    url(r'^admin_roles/$', admin_rol, name='admin_rol'),
    url(r'^add_rol/$', add_rol, name='add_rol'),
    #para manejar urls del tipo "/rol/<nombre_rol>" para editarlos
    url(r'^roles/(?P<rol_name>\w+)/$', edit_rol, name='edit_rol'),
    url(r'^roles/delete/(?P<rol_name>\w+)/$', delete_rol, name='edit_rol'),
    url(r'^asignar_rol/$', asignar_rol, name='asignar_rol'),



    url(r'^admin_proyectos/$', 'proyecto.views.admin_proyecto'),
    url(r'^add_proyecto/$','proyecto.views.add_proyecto' ),
    url('proyectos/(\d+)/', 'proyecto.views.proyecto_detail', name='proyecto_detail'),
    url('proyectos/delete/(\d+)/', 'proyecto.views.delete_proyecto', name='delete_proyecto'),
    url('proyecto_view/(\d+)/', 'proyecto.views.proyecto_view', name='proyecto_view'),
    url('proyectos/fases/(\d+)/', 'proyecto.views.fase_detail', name='fase_detail'),
    url('proyectos/fases/delete/(\d+)/', 'proyecto.views.delete_fase', name='delete_fase'),
    url('proyectos/fases/importar_fase/(\d+)/', 'proyecto.views.importar_fase', name='importar_fase'),

    url(r'^admin_tipoitem/$', admin_tipoitem, name='admin_tipoitem'),
    url(r'^add_tipoitem/$', add_tipoitem, name='add_tipoitem'),
    url(r'^add_atributo/$', add_atributo, name='add_atributo'),
    url(r'^listar_atributos/$', listar_atributos, name='listar_atributos'),
    url(r'^edit_tipoitem/(?P<tipoitem_id>\d+)/$', edit_tipoitem, name='edit_tipoitem'),
    url(r'^edit_atributo/(?P<atributo_id>\d+)/$', edit_atributo, name='edit_atributo'),
    url(r'^delete_tipoitem/(?P<tipoitem_id>\d+)/$', delete_tipoitem, name='delete_tipoitem'),
    url(r'^delete_atributo/(?P<atributo_id>\d+)/$', delete_atributo, name='delete_atributo'),
    url(r'^importar_tipoitem/$', importar_tipoitem, name='importar_tipoitem'),



    url(r'^item/', include('item.urls')),








)
