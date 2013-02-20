
class Apps(object):
    """ App configuration """
    
    DJANGO_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    
        # Useful template tags:
        # 'django.contrib.humanize',
    
        # Admin panel and documentation:
        'django.contrib.admin',
        # 'django.contrib.admindocs',
    )
    
    THIRD_PARTY_APPS = (
        # Database migration helpers:
        'south',
    )
    
    # Apps specific for this project go here.
    PROJECT_APPS = (
    )
    
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

    
class AppsDebug(object):
    """ App configuration plus Debug toolbar """
    
    # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
    INSTALLED_APPS = Apps.INSTALLED_APPS + (
        'debug_toolbar',
    )
    