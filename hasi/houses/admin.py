# -*- coding: utf-8 -*-
#
# Erstellt von Martin Gutmair
# modified 04.05.2011
#

from hasi.houses.models import House, Room
from django.contrib import admin

# list_display bestimmt immer welche Felder auf der Übersicht angezeigt werden

class RoomInline(admin.TabularInline):
# Die Klasse RoomInline ermöglicht es, in Adminseite von Houses, die 
# Adminseite von Rooms zu integrieren. Es wird außerdem definiert, dass
# immer 3 neue Reihen angezeigt werden

    prepopulated_fields = {"slug": ("name",)}
    model = Room
    extra = 3


class HouseAdmin(admin.ModelAdmin):
# Damit RoomInline auch aufgerufen wird, muss er in inlines als !tupel!
# zugewiesen werden. prepopulated_fields erzeugt automatisch den Slug mithilfe
# des Namens

    inlines = [RoomInline]
    prepopulated_fields = {"slug": ("name",)}


class RoomAdmin(admin.ModelAdmin):
# prepopulated_fields erzeugt automatisch den Slug mithilfe des Namens
    list_display = ('name', 'house')
    prepopulated_fields = {"slug": ("name",)}
    
  
# Anschließend müssen alle benötigten Adminseiten registriert werden
admin.site.register(House, HouseAdmin)
admin.site.register(Room, RoomAdmin)
    
