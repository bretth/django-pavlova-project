#!/usr/bin/env python
import os
import site
import sys

if __name__ == "__main__":
      
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'DevSettings')
    site.addsitedir('project')
    
    import {{ project_name }}.startup as startup

    startup.run()

    from configurations.management import execute_from_command_line


    execute_from_command_line(sys.argv)