from os.path import join, normpath
from urlparse import urlparse, uses_netloc

from djset import secret

from .base import DJANGO_ROOT, SITE_ROOT


uses_netloc.append('postgres')


class SqliteDB(object):
    
    def DATABASES(self):
        return {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
                        'USER': '',
                        'PASSWORD': '',
                        'HOST': '',
                        'PORT': '',
                    }
                }


class PostgresDB(object):
    
 
    def DATABASES(self):

        url = urlparse(
            secret.get('DATABASE_URL',
                       'postgres://vagrant:vagrant@localhost:6432/',
                       'Postgresql database url')
        )
        return {
                    'default': {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2',
                        'NAME': url.path[1:],
                        'USER': url.username,
                        'PASSWORD': url.password,
                        'HOST': url.hostname,
                        'PORT': url.port,
                    }
                }
    
    
class Fixtures(object):
    """ Fixture Configuration """
    # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
    FIXTURE_DIRS = (
        normpath(join(SITE_ROOT, 'fixtures')),
    )
    
    
    