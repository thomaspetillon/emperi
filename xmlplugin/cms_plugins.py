from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import XmlPlugin
import urllib2
import json
import os
from datetime import datetime 
from django.utils.translation import ugettext as _
from django.core import serializers
from django.core.cache import cache

class CMSXmlPlugin(CMSPluginBase):
    here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
    model = XmlPlugin
    name = _("Xml Plugin")
    render_template = here("templates/plugins/default.html")

    def render(self, context, instance, placeholder):
        #debug
        print "--> xmlplugin"
        begin = datetime.now()

        if instance.template :
            self.render_template = instance.template   
        req = urllib2.Request(instance.source) if instance.source else urllib2.Request('http://null.null')
        
        d= cache.get(instance.source)
        if not d:
            print "no cache found for "+instance.source+"\n get source ..."
            r = urllib2.urlopen(req)
            d = r.read()
            cache.set(instance.source,d,1800) # todo : use a cache time field
            print "cache create : "+instance.source
        
        datas = json.loads(d) if (instance.datatype == "json") else [ {u'data type' : u'xml',u'Implement' : u'Not Yet'}]

        #debug
        print "duration "
        print datetime.now() - begin
        print "<-- xlmplugin"
        
        context.update({
                'datas':datas,
                'object':instance,
                'placeholder':placeholder
            })
        return context

plugin_pool.register_plugin(CMSXmlPlugin)