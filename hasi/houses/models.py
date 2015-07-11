# -*- coding: utf-8 -*-
#
# Erstellt von Martin Gutmair
# modified 05.05.2011
#
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime



# Jede Klasse bekommt die Werte created und modified, welche den Erstellungs und
# Änderungszeitpunkt enthält

# get_absolute_url erstellt die absolute Url zu dem jeweiligen Objekt
# __unicode__ gibt den Namen des Objekts zurück

class House(models.Model):
# House ist wie der Name schon sagt ein Haus. Es besteht wie alle Objekte aus einem
# Namen sowie einem Slug

    name = models.CharField(_(u'Name'), max_length=255)
    slug = models.SlugField(_(u'Slug'), max_length=100, unique=True)

    created = models.DateTimeField(default=datetime.now, editable=False)
    modified = models.DateTimeField(default=datetime.now, auto_now=True, editable=False)
    
    @models.permalink
    def get_absolute_url(self):
        return 'house', (), { 'slug': self.slug }
    
    def __unicode__(self):
            return self.name
            
class Room(models.Model):
# Room ist wie der Name schon sagt ein Raum. Er besteht wiederrum aus einem Namen,
# einem Slug und zeigt auf ein Haus

    house = models.ForeignKey('House', null=True, related_name='rooms')
    name = models.CharField(_(u'Name'), max_length=255)
    slug = models.SlugField(_(u'Slug'), max_length=100)

    created = models.DateTimeField(default=datetime.now, editable=False)
    modified = models.DateTimeField(default=datetime.now, auto_now=True, editable=False)

    @models.permalink
    def get_absolute_url(self):
        return 'room', (), { 'slug': self.slug }
    
    def __unicode__(self):
            return self.house.name + ' - ' + self.name
          

