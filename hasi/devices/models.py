# -*- coding: utf-8 -*-
#
# Erstellt von Martin Gutmair
# modified 04.05.2011
#

from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from hasi.houses.models import Room



# Jede Klasse bekommt die Werte created und modified, welche den Erstellungs und
# Änderungszeitpunkt enthält

# get_absolute_url erstellt die absolute Url zu dem jeweiligen Objekt
# __unicode__ gibt den Namen des Objekts zurück


class Device(models.Model):
# Device ist das Gerät an dem die Subdevices (z.B Messgeräte angeschlossen sind)
# Es besteht aus einem Name und einem Slug. Der Slug ist die eindeutige Bezwichnugn
# des Gerätes, er besteht ohne Leerzeichen, Umlaute usw. Siehe SlugField
# http://docs.djangoproject.com/en/1.3/ref/forms/fields/#slugfield

    name = models.CharField(_(u'Name'), max_length=255)
    slug = models.SlugField(_(u'Slug'), max_length=100, unique=True)

    created = models.DateTimeField(default=datetime.now, editable=False)
    modified = models.DateTimeField(default=datetime.now, auto_now=True, editable=False)
 
    @models.permalink
    def get_absolute_url(self):
        return 'device', (), { 'slug': self.slug }
    
    def __unicode__(self):
            return self.name


class Subdevice(models.Model):
# Subdevices ist ein Sensor eines Gerätes. Er besteht wieder aus einem Namen und 
# Slug (Siehe oben). Außerdem bekommt jedes Subdevice einen Typ wie z.B Schaltbare 
# Steckdose oder Strommessgerät. Jedes Subdevice wird außerdem eindeutig einem 
# Device und Raum zugeordnet (Raum kann NULL sein)    

    device = models.ForeignKey('Device', null=True, related_name='subdevices')
    name = models.CharField(_(u'Name'), max_length=255)
    slug = models.SlugField(_(u'Slug'), max_length=100)
    room = models.ForeignKey('houses.Room', null=True, related_name='subdevices')
    model = models.ForeignKey('Model', null=True, related_name='subdevices')

    created = models.DateTimeField(default=datetime.now, editable=False)
    modified = models.DateTimeField(default=datetime.now, auto_now=True, editable=False)
 
    @models.permalink
    def get_absolute_url(self):
		return 'subdevice_detail', (), { 'subdeviceslug': self.slug, 'deviceslug': self.device.slug }
    
    def __unicode__(self):
            return self.name
            

class Model(models.Model):
# Model beschreibt den Type des Subdevices ( Ich nehme Model, da "type" in Python
# schon vergeben ist. Model besteht wieder aus einem Namen sowie einem Slug
# Der Slug ist auch gleichzeitig der Name des für diesen Typ benötigtem Template
    
    name = models.CharField(_(u'Name'), max_length=255)
    slug = models.SlugField(_(u'Slug'), max_length=100, unique=True)
    
    created = models.DateTimeField(default=datetime.now, editable=False)
    modified = models.DateTimeField(default=datetime.now, auto_now=True, editable=False)
    
    @models.permalink
    def get_absolute_url(self):
        return 'model', (), { 'slug': self.slug }
    
    def __unicode__(self):
            return self.name
            
    def include_template(self):
    # Diese Funktion ladet je nach Model das richtige Template
        return"gadgets/model/" + self.slug + ".html"
 
 
class Measurement(models.Model):
# Die Klasse Measurement ist für die Speicherung der Daten jedes Subdevices zuständig
# Sie besteht aus einem eindeutigen Subdevice, einem Wert, dem Beginn und dem Ende 
# des Eintrags

    subdevice = models.ForeignKey('Subdevice', null=False, related_name='measurements')
    value = models.CharField(_(u'Value'), max_length=255)
    begin = models.DateTimeField(editable=True)
    end = models.DateTimeField(editable=True)
    
    def __unicode__(self):
            return self.begin.__str__() + ' - ' + self.end.__str__()
            
    

