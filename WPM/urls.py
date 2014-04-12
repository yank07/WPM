from django.conf.urls import patterns, include, url

from django.contrib import admin
from principal.views import add_proyecto, admin_proyecto, admin_rol, add_rol, asignar_rol

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WPM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'principal.views.ingresar', name='home'),
    url(r'^ingresar/$','principal.views.ingresar'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_proyectos/$', admin_proyecto, name='admin_proyecto'),
    url(r'^add_proyecto/$', add_proyecto, name='add_proyecto'),

    url(r'^nuevo_usuario/$', 'principal.views.nuevo_usuario'),
    url(r'^nuevo_usuario/perfil$', 'principal.views.user_profile'),
      url(r'^cerrar/$','principal.views.cerrar'),

    url(r'^admin_roles/$', admin_rol, name='admin_rol'),
    url(r'^add_rol/$', add_rol, name='add_rol'),
    url(r'^asignar_rol/$', asignar_rol, name='asignar_rol'),


)
