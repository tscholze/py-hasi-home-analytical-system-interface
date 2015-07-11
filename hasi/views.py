# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout

def home(request):
    #return HttpResponse("Hasi Home")
    return render_to_response('base.html', context_instance = RequestContext(request))

def index(request):
    #return HttpResponse("Hasi Home")
    return render_to_response('index.html', context_instance = RequestContext(request))
    
def login(request):
    return render_to_response('user/login-base.html', context_instance = RequestContext(request))
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index.html')
    

