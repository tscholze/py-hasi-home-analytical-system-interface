# -*- coding: utf-8 -*-
#
# Erstellt von Martin Gutmair
# modified 05.05.2011
#

from hasi.gadgets.models import Gadget, GadgetSubdevice, UserGadget
from django.contrib.auth.models import User
from django.contrib import admin

# list_display bestimmt immer welche Felder auf der Übersicht angezeigt werden

class GadgetSubdeviceInline(admin.TabularInline):
# Die Klasse GadgetSubdeviceInline ermöglicht es, in Adminseite von Gadget, die 
# Adminseite von GadgetSubdevice zu integrieren. Es wird außerdem definiert, dass
# immer 1 neue Reihe angezeigt werden

    model = GadgetSubdevice
    extra = 1
    
class UserGadgetInline(admin.TabularInline):
# Die Klasse GadgetSubdeviceInline ermöglicht es, in Adminseite von Gadget, die 
# Adminseite von UserGadget zu integrieren. Es wird außerdem definiert, dass
# immer 1 neue Reihe angezeigt werden

    model = UserGadget
    extra = 1

class GadgetAdmin(admin.ModelAdmin):
# Damit GadgetSubdeviceInline und UserGadgetInline auch aufgerufen werden, 
# müssen sie in inlines als !tupel! zugewiesen werden

    list_display = ('name', 'description')
    inlines = [GadgetSubdeviceInline, UserGadgetInline]
    prepopulated_fields = {"slug": ("name",)}
    
    
# Anschließend müssen alle benötigten Adminseiten registriert werden
admin.site.register(Gadget, GadgetAdmin)
