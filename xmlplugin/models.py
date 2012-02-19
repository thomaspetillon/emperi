from django.db import models
from cms.models import CMSPlugin
from django.core import serializers
import urllib2
import json
from django.conf import settings
from django.utils.translation import ugettext_lazy as _, get_language, ugettext

# Create your models here.

datatype_choice =[
	('json','JSON'),
	('xml','XML'),
]

class XmlPlugin(CMSPlugin):
	template_choices = [(x, _(y)) for x,y in settings.XMLPLUGIN_TEMPLATES]
	name = models.CharField(_("name"), max_length=100)
	source = models.URLField()
	datatype = models.CharField(_("Data Type"), max_length=10,choices=datatype_choice,help_text=_('Select appropriate type of incoming datas'))
        template = models.CharField(_("template"), max_length=255, choices=template_choices, help_text=_('The template used to render the content.'), blank = True)

# Create your views here.




