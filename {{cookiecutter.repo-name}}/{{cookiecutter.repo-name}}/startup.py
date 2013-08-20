"""
startup.py

You would call this file from manage.py and wsgi.py to do stuff before django otherwise loads.
"""
from djset import secret, config
from djset.utils import getbool

from django.conf import settings
from django.utils.importlib import import_module
from django.utils.module_loading import module_has_submodule

secret.prompt = getbool('SETTINGS_PROMPT', True)
config.prompt = secret.prompt

def autoload(submodules):
    """ load modules that aren't normally imported """
    for app in settings.INSTALLED_APPS:
        mod = import_module(app)
        for submodule in submodules:
            try:
                import_module("{}.{}".format(app, submodule))
            except:
                if module_has_submodule(mod, submodule):
                    raise


def run():
    autoload(["receivers"])