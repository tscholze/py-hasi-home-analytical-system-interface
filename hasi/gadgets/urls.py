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

urlpatterns = patterns('hasi.gadgets.views',
    url(r'^gadgets.html$', 'gadgets', name="gadgets"),
)
