import sys

class Middleware(object):
    """ Middleware Configuration """
    
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
    MIDDLEWARE_CLASSES = (
        # Default Django middleware.
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )


class MiddlewareDebug(object):
    if sys.version_info.major == 2:
        # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
        MIDDLEWARE_CLASSES = Middleware.MIDDLEWARE_CLASSES + (
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        )
        # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
        INTERNAL_IPS = ('127.0.0.1',)
