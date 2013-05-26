# these settings may be imported by any settings file
from os.path import abspath, basename, dirname

PROJECT_ROOT = dirname(dirname(abspath(__file__)))

PACKAGES_ROOT = dirname(PROJECT_ROOT)

SITE_ROOT = dirname(PACKAGES_ROOT)

# Site name:
SITE_NAME = '{{ project_name }}'

