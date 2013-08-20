try:
    __version__ = __import__('pkg_resources').get_distribution('djangoproject').version
except:
    __version__ = ''

try:
    name = __import__('pkg_resources').get_distribution('djangoproject').name
except:
    name = ''