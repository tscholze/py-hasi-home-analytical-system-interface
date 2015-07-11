# -*- coding: utf-8 -*-
#
# Erstellt von Martin Gutmair
# modified 04.05.2011
#

import os.path
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.conf.urls.defaults import *
from hasi.gadgets.models import Gadget, GadgetSubdevice, UserGadget

urlpatterns = patterns('hasi.devices.views',
	url(r'^detail/(?P<deviceslug>[a-z0-9_-]+)/(?P<subdeviceslug>[a-z0-9_-]+)\.html$', 'subdevice_detail', name="subdevice_detail" ),
                     
)
