# -*- coding: utf-8 -*-
#
# Erstellt von Martin Gutmair
# modified 04.05.2011

from django.db import models
from hasi.devices.models import Subdevice
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime

# Jede Klasse bekommt die Werte created und modified, welche den Erstellungs und
# Änderungszeitpunkt enthält

# __unicode__ gibt den Namen des Objekts zurück


class Gadget(models.Model):
# Ein Gadget ist auf der Personalisierten Seite ein Bereich, der Mehrere Subdevices
# enthalten kann. Er besteht aus einem Namen, einem eindeutigem Slug
# (http://docs.djangoproject.com/en/1.3/ref/forms/fields/#slugfield) und einer Beschreibung,
# Auf die zugewiesenen Subdevices bzw. User kann durch die related_names "gadgetsubdevice'
# bzw. usergadget zugegriffen werden.

    name = models.CharField(_(u'Name'), max_length=255)
    slug = models.SlugField(_(u'Slug'), max_length=100, unique=True)
    description = models.CharField(_(u'Beschreibung'), max_length=255)

    created = models.DateTimeField(default=datetime.now, editable=False)
    modified = models.DateTimeField(default=datetime.now, auto_now=True, editable=False)
 
    def __unicode__(self):
            return self.name

class GadgetSubdevice(models.Model):
# GadgetSubdevice stellt dir Relation zwischen den Gadgets und Subdevices her. 
# Neben dem Gadget und dem Subdevice kann hier noch eine Dezimalzahl für die Reihenfolge angegeben werden 
# 0 = ganz oben, 99 = ganz unten. Ordering sortiert die Liste

    subdevice = models.ForeignKey('devices.Subdevice', related_name='gadgetsubdevice')
    order = models.DecimalField(_('Reihenfolge'), max_digits=2, decimal_places=0, blank=False, null=False)
    gadget = models.ForeignKey('Gadget', related_name='gadgetsubdevice')
    
    def __unicode__(self):
            return self.subdevice.name
            
    class Meta:
        ordering = ['order']                
    
    created = models.DateTimeField(default=datetime.now, editable=False)
    modified = models.DateTimeField(default=datetime.now, auto_now=True, editable=False)
 
class UserGadget(models.Model):
# UserGadget stellt die Relation zwischen User und Gadget her. Hier können die User,
# welche das Gadget sehen wollen, es ihrem Namen zuordnen, die Position (Links, Mitte Rechts)
# und die Reihenfolge (0 = Oben, 99 = Unten) angeben. Ordering sortiert die Liste

    POSITION_LEFT = 0
    POSITION_CENTERT = 10
    POSITION_RICHT = 20
    POSITION_CHOICES = (
        (POSITION_LEFT, _('links')),
        (POSITION_CENTERT, _('mitte')),
        (POSITION_RICHT, _('rechts')),
    )
    users = models.ForeignKey(User, related_name='usergadget')
    gadget = models.ForeignKey('Gadget', related_name='usergadget')
    position = models.IntegerField(_(u'Position'), choices=POSITION_CHOICES)
    order = models.DecimalField(_('Reihenfolge'), max_digits=2, decimal_places=0, blank=False, null=False)
    
    created = models.DateTimeField(default=datetime.now, editable=False)
    modified = models.DateTimeField(default=datetime.now, auto_now=True, editable=False)
    
    def __unicode__(self):
            return self.users.username
 
    class Meta:
        ordering = ['users']                
    

