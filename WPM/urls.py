from django.conf.urls import patterns, include, url

from django.contrib import admin
from principal.views import add_proyecto
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WPM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'principal.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_proyecto/$', add_proyecto, name='add_proyecto'),
)
