# -*- coding: utf-8 -*-
#
# Erstellt von Martin Gutmair
# modified 04.05.2011
#

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User


from hasi.gadgets.models import Gadget, GadgetSubdevice, UserGadget

def gadgets(request):
# Ladet Userspezifisch die Gadgets in die richtigen Spalten und übergibt sie an
# das Template. Falls kein User eingeloggt ist, kommt "Nicht eingeloggt"
    if(request.user.is_authenticated()):
        gadgets = Gadget.objects.filter(usergadget__users=request.user)
        gadgets_left = gadgets.filter(usergadget__position=0)
        gadgets_center = gadgets.filter(usergadget__position=10)
        gadgets_right = gadgets.filter(usergadget__position=20)
    
        return render_to_response(
            'gadgets/index.html', 
            {'gadgets_left': gadgets_left,         
            'gadgets_center': gadgets_center,         
            'gadgets_right': gadgets_right},         
            context_instance = RequestContext(request))
    else:
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login.html?next=%s' % request.path)
        
