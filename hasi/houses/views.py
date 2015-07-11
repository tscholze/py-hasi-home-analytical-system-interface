# -*- coding: utf-8 -*-
#
# Erstellt von Martin Gutmair
# modified 05.05.2011
#

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from hasi.houses.models import House, Room

def house_list(request):
    houses = House.objects.all()
    print houses
    
    return render_to_response(
        'houses/index.html', 
        {'houses': houses},         
        context_instance = RequestContext(request))
