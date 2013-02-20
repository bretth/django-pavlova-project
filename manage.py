#!/usr/bin/env python
import os
import site
import sys

if __name__ == "__main__":
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'DevSettings')
    site.addsitedir('project')

    from djset import secret, config
    dj_config = os.getenv('DJANGO_CONFIGURATION')
    # Prompt for development, raise error or use defaults for other
    secret.prompt = dj_config == 'DevSettings'
    config.prompt = secret.prompt

    from configurations.management import execute_from_command_line


    execute_from_command_line(sys.argv)