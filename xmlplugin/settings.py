import os

here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

PLUGIN_DEFAULT_TEMPLATE = [ here('templates/plugins/default.html'),]

XMLPLUGIN_TEMPLATE = [ ]
