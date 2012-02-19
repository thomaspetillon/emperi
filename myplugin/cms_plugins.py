from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import MyPlugin
from models import OEmbedPlugin
from models import RemoteXmlPlugin
from django.utils.translation import ugettext as _
import urllib2
import json

class CMSMyPlugin(CMSPluginBase):
    model = MyPlugin
    name = _("Topic Plugin")
    render_template = "myplugin.html"

    def render(self, context, instance, placeholder):
        context.update({            
            'object':instance,
            'placeholder':placeholder
        })
        return context
    
class CMSRemoteXmlPlugin(CMSPluginBase):
    model = RemoteXmlPlugin
    name = _("Remote XML plugin")
    render_template = "remote_xml_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({            
            'object':instance,
            'webservice':instance.webservice,
            'stylesheet':instance.stylesheet,
            'placeholder':placeholder
        })
        return context
    
class CMSOEmbedPlugin(CMSPluginBase):
    model = OEmbedPlugin
    name = _("OEmbed plugin")
    render_template = "oembed_plugin.html"

    def render(self, context, instance, placeholder):
        # Call url
        sock   = urllib2.urlopen(instance.url)
        result = sock.read()
        html = json.loads(result)["html"]
        context.update({            
            'object':instance,
            'html':html,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSMyPlugin)
plugin_pool.register_plugin(CMSOEmbedPlugin)
plugin_pool.register_plugin(CMSRemoteXmlPlugin)