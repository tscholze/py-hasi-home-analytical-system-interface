# -*- coding: utf-8 -*-
#
# Erstellt von Martin Gutmair
# modified 06.05.2011
#

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User

from hasi.devices.models import Device, Subdevice, Model, Measurement

def subdevice_detail(request, deviceslug, subdeviceslug):
    subdevice = get_object_or_404(Subdevice, slug=subdeviceslug, device__slug=deviceslug)
    return render_to_response(
      'devices/subdevice-detail.html', 
      {'subdevice': subdevice}, 
      context_instance = RequestContext(request) 
    )
