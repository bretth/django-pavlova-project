from os.path import join, normpath

from .base import SITE_ROOT


class LocalStatic(object):
    """ Static File Configuration """
    
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = normpath(join(SITE_ROOT, '.collectedstatic'))
    
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'
    
    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        normpath(join(SITE_ROOT, 'static')),
    )
    

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )


class LocalMedia(object):
    """ Media Configuration """    

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
    
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'   
    


    

    


