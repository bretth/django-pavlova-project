django-pavlova-project
=======================

A zero configuration project template for Django 1.5 using django-configurations_ for class based settings and djset_ for secret setting management. Structured to play nice with frontend javascript frameworks.

Requirements
-------------

The bar is low. This project assumes you are using *virtualenv*, and virtualenvwrapper_. The quickstart bootstrap script and install command is for a posix based system, and we use *curl* to download it.

Creating your project
-----------------------

To create a project called ``dessert``, bootstrap it..

.. code-block:: bash

    $ mkproject dessert
    $ sh <(curl -s https://raw.github.com/bretth/django-pavlova-project/master/bootstrap.sh) dessert

or for the development version of django.

.. code-block:: bash

    $ sh <(curl -s https://raw.github.com/bretth/django-pavlova-project/master/bootstrap.sh) dessert --dev

A superuser is created by default (in development only) with the login and password ``admin``.

If everything went well, open your browser and point to the django admin:

    http://localhost:8000/admin/

You should replace this README with your own.

Deployment Notes
------------------

Project deployment is out of scope for this template, but you should only need to change one environment variable in production ``DJANGO_CONFIGURATION=ProductionSettings``. You can also set ``SETTINGS_PROMPT=False`` if you don't want to be prompted for missing secrets (and have an error raised instead).

Unlike some recommendations to use django-admin.py in production, you will need to use *manage.py*. You can edit that to customize environment variables defaults before settings are loaded.

    
Project Template Notes
------------------------
The pavlova project templates is intended for larger projects where the standard django settings can become an anti-pattern. Specifically we're trying to avoid:

 - Long settings files
 - if else DEBUG settings
 - Diverging production and development/testing settings
 - non-versioned local development settings
 - commenting out blocks of settings to switch configuration
 - the settings file shuffle when injecting a new app's configuration, otherwise known as 'where in the world does this setting go'.

Pavlova uses the sqlite3 database for a quickstart however switching to postgresql is recommended for all but the smallest projects.

A minimal setup.cfg and setup.py is used to install the project in the path in ``develop`` mode, and hold project metadata.

A *dev* app holds local fixtures (or factory objects) for loading into the development environment starting with a superuser.


Acknowledgements
-----------------

The django-pavlova-project draws on the excellent https://github.com/twoscoops/django-twoscoops-project/ for it's thoughtful layout and some base settings... which we then break.

.. _django-configurations: https://github.com/jezdez/django-configurations/
.. _djset: https://github.com/bretth/djset
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org
