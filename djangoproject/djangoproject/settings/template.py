from os.path import join, normpath

from .base import SITE_ROOT

class Template(object):
    """ Template Configuration """
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
    )
    
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        )),
    )
    
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        normpath(join(SITE_ROOT, 'templates')),
    )


