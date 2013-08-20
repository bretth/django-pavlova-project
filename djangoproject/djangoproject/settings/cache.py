
class LocalMemCache(object):

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }
    
    
class DummyCache(object):
    
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

