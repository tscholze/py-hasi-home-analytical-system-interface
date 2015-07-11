# -*- coding: utf-8 -*-
#
# Erstellt von Martin Gutmair
# modified 05.05.2011
#

import os.path
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *

from hasi.houses.models import House, Room

urlpatterns = patterns('hasi.houses.views',
    url(r'^house_list.html$', 'house_list', name="house_list"),
)
