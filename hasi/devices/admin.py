# -*- coding: utf-8 -*-
#
# Erstellt von Martin Gutmair
# modified 04.05.2011
#

from hasi.devices.models import Device, Subdevice, Model, Measurement
from django.contrib import admin

# list_display bestimmt immer welche Felder auf der Übersicht angezeigt werden

class SubdeviceInline(admin.TabularInline):
# Die Klasse SubdeviceInline ermöglicht es, in Adminseite von Device, die 
# Adminseite von Subdevice zu integrieren. Es wird außerdem definiert, dass
# immer 3 neue Reihen angezeigt werden

    model = Subdevice
    extra = 5

class DeviceAdmin(admin.ModelAdmin):
# Damit SubdeviceInline auch aufgerufen wird, muss er in inlines als !tupel!
# zugewiesen werden

    list_display = ('name', 'slug')
    inlines = [SubdeviceInline]
   
   
class SubdeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'room', 'slug')


class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('subdevice', 'value', 'begin', 'end')

    
# Anschließend müssen alle benötigten Adminseiten registriert werden
admin.site.register(Device, DeviceAdmin)
admin.site.register(Subdevice, SubdeviceAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Measurement, MeasurementAdmin)
    
