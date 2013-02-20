from djset import config, secret

from .base import SITE_NAME


class EmailSMTP(object):
    """ Email configuration """
    
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    

    def EMAIL_HOST(self):
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
        return config.get('EMAIL_HOST', 'smtp.gmail.com')

    def EMAIL_HOST_PASSWORD(self):
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
        return secret.get('EMAIL_HOST_PASSWORD', '')
    
    def EMAIL_HOST_USER(self):
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
        return config.get('EMAIL_HOST_USER', 'your_email@example.com')

    def EMAIL_PORT(self):
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
        return config.get('EMAIL_PORT', 587)
    
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
    EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
    
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
    EMAIL_USE_TLS = True
    
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
    SERVER_EMAIL = EMAIL_HOST_USER

        
    
class EmailConsole(object):
    """ Email backend for development """
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    

class EmailInMemory(object):
    """ Email backend for Testing """
    
    EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
