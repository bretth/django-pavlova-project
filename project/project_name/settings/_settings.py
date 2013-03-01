
from configurations import Settings
from djset import config, secret

from .apps import Apps, AppsDebug
from .cache import LocalMemCache, DummyCache
from .db import PostgresDB, SqliteDB, Fixtures
from .email import EmailSMTP, EmailConsole, EmailInMemory
from .locale import Locale
from .logging import LoggingSendEmail
from .middleware import Middleware, MiddlewareDebug
from .staticmedia import LocalMedia, LocalStatic
from .template import Template

class BaseSettings(
    Apps,
    Fixtures,
    SqliteDB,
    Locale,
    Template,
    LocalMedia,
    LocalStatic,
    Middleware,
    Settings):
    
    SITE_ID = 1

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    SECRET_KEY = r"{{ secret_key }}"
    
    ROOT_URLCONF = '{{ project_name }}.urls'


class ProductionSettings(
    # PostgresDB,
    EmailSMTP,
    LoggingSendEmail,
    BaseSettings):
    
    def SECRET_KEY(self):
        return secret.get('SECRET_KEY')

    def ADMINS(self):
        adm_help = "See: https://docs.djangoproject.com/en/dev/ref/settings/#admins"
        admins = (
            (config.get('ADMINS_NAME', 'admin', adm_help),
             config.get('ADMINS_EMAIL', 'admin@example.com', prompt_help=adm_help),
            )
        )
        return admins

    def MANAGERS(self):
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
        return self.ADMINS()
    
    def SECRET_KEY(self):
        return secret.get('SECRET_KEY')

      
class DevSettings(
    AppsDebug,
    LocalMemCache,
    EmailConsole,
    # Add Logging class
    MiddlewareDebug,
    BaseSettings):
    
    DEBUG = True
    TEMPLATE = DEBUG
    
    def INSTALLED_APPS(self):
        return super(DevSettings, self).INSTALLED_APPS + (
        'dev',
    )

class TestSettings(
    EmailInMemory, 
    DummyCache,
    BaseSettings):
    
    pass
