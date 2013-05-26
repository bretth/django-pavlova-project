try:
    __version__ = __import__('pkg_resources').get_distribution('djangoproject').version
except:
    __version__ = ''