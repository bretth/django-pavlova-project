
class Apps(object):
    """ App configuration """

    # Apps that always come first
    BOOTSTRAP_APPS = (
    )
    
    # Django and third party apps 
    BASE_APPS = (
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

         # Database migration helpers:
        'south',
    )
    
    # Apps specific for this project (other than bootstrap apps).
    PROJECT_APPS = (
    )
    
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = BOOTSTRAP_APPS + BASE_APPS + PROJECT_APPS

    
class AppsDebug(object):
    """ App configuration plus Debug toolbar """
    
    # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
    INSTALLED_APPS = Apps.INSTALLED_APPS + (
        'debug_toolbar',
    )
    