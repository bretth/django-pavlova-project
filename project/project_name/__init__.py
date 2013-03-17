__version__ = '0.0'


def version_hook(config):
    config['metadata']['version'] = __version__