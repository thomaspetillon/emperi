# -*- coding: utf-8 -*-
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

gettext = lambda s:s

import locale #for date time conversion in templatetags
#locale.setlocale(locale.LC_ALL, ('fr_FR', 'UTF8'))
#locale.setlocale(locale.LC_ALL,'')

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Thomas Petillon', 'petillon@topic.fr'),
)

MANAGERS = ADMINS

LANGUAGES = [('fr', gettext('French'))]
DEFAULT_LANGUAGE = 0

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-FR'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'public/static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0r6%7gip5tmez*vygfv+u14h@4lbt^8e2^26o#5_f_#b7%cm)u'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'files'),    
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',

)

CMS_TEMPLATES = (
     ('article_base.html', 'Article standard'),
     ('article_liste.html', 'Article avec liste'),
     ('article_fiche.html', 'Article avec Fiches'),     
     ('article_partenaires.html', 'Page Partenaires'),
     ('accueil.html', 'Accueil'),
     ('structure.html', 'Structure'),
)

XMLPLUGIN_TEMPLATES = (
	 ('plugins/artiste.html', 'Artistes (tous)'),
	 ('plugins/programme_detail.html', 'Programme'),
	 ('plugins/programme_titre.html', 'Programme Succinct'),
         ('plugins/programme_info_ce_soir.html', 'Sous-Titre'),
)

CMS_PLACEHOLDER_CONF = {
    'carousel': {
        'plugins': ('TextPlugin','CarouselPlugin'),
        'name': gettext("Caroussel dynamique")
    },
    'info1': {
        'plugins': ('CMSXmlPlugin','FilePlugin', 'FlashPlugin', 'LinkPlugin', 'PicturePlugin', 'TextPlugin', 'SnippetPlugin','GoogleMapPlugin','CMSTextWithTitlePlugin','CMSGalleryPlugin'),
        'name': gettext("Bas de page, gauche")
    },
    'info2': {
        'plugins': ('CMSXmlPlugin','FilePlugin', 'FlashPlugin', 'LinkPlugin', 'PicturePlugin', 'TextPlugin', 'SnippetPlugin','GoogleMapPlugin','CMSTextWithTitlePlugin','CMSGalleryPlugin'),
        'name': gettext("Bas de page, centre")
    },
    'info3': {
        'plugins': ('CMSXmlPlugin','FilePlugin', 'FlashPlugin', 'LinkPlugin', 'PicturePlugin', 'TextPlugin', 'SnippetPlugin','GoogleMapPlugin','CMSTextWithTitlePlugin','CMSGalleryPlugin'),
        'name': gettext("Bas de page, droite")
    },
    'main': {
        'plugins': ('TopicPlugin','CMSXmlPlugin','FilePlugin', 'FlashPlugin', 'LinkPlugin', 'PicturePlugin', 'TextPlugin', 'SnippetPlugin','GoogleMapPlugin','CMSTextWithTitlePlugin','CMSGalleryPlugin'),
        'name': gettext("Page")
    },
     'header_info': {
        'plugins': ('TextPlugin','LinkPlugin','CMSXmlPlugin',),
        'name': gettext("Block Info sous-titre")
    },
     'footer1': {
        'plugins': ('TextPlugin','LinkPlugin'),
        'name': gettext("Pied De Page 1")
    },
     'footer2': {
        'plugins': ('TextPlugin','LinkPlugin'),
        'name': gettext("Pied De Page 2")
    },
     'footer3': {
        'plugins': ('TextPlugin','LinkPlugin'),
        'name': gettext("Pied De Page 3")
    },
}
CMS_PLUGIN_PROCESSORS = (
    'cms_plugin_processors.carousel',
)


ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'cms',
    'menus',
    'mptt',
    'appmedia',
    'south',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'myplugin',
    'xmlplugin',
    'sekizai'
)

# local settings that'll overload the settings defined here
try:
    from local_settings import *
except ImportError:
    pass
