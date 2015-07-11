# -*- coding: utf-8 -*-
import os.path
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hasi.views.index', name='index'),
    url(r'^index.html$', 'hasi.views.index', name='index'),
    url(r'^logout.html$', 'hasi.views.logout_view', name='logout'),
    url(r'^login.html$', 'django.contrib.auth.views.login', {'template_name': 'user/login-base.html'}, name='login'),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    
    
    url(r'^list_devices', 'hasi.views.index',include('list_devices.urls')),
    url(r'^$', direct_to_template,{"schedule":"homepage.html"}), (r'^schedule/', include('schedule.urls')),
    url(r'^', include('hasi.gadgets.urls')),
    url(r'^', include('hasi.houses.urls')),
    url(r'^', include('hasi.devices.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)



if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

