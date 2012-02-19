from django.db import models
from cms.models import CMSPlugin

class MyPlugin(CMSPlugin):
    pass

class RemoteXmlPlugin(CMSPlugin):
    webservice = models.URLField()
    stylesheet = models.URLField()
    
class OEmbedPlugin(CMSPlugin):
    url = models.URLField()    
