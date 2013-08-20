from os.path import join, normpath
try:
    from urlparse import urlparse, uses_netloc
except ImportError:
    from urllib.parse import urlparse, uses_netloc
import sys

from djset import secret

uses_netloc.append('postgres')


class SqliteDB(object):
    
    def DATABASES(self):
        return {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': normpath(join(sys.prefix, 'default.db')),
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
    
    
    
    