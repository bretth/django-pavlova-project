django-pavlova-project
=======================

A project template for Django 1.5 using django-configurations for class based settings and djset for secret setting management.

Creating your project
----------------------

First, make sure you are using virtualenv, and virtualenvwrapper (http://virtualenvwrapper.readthedocs.org). To create a project called ``dessert`` you can bootstrap it the short way with a bash script or the slightly longer way. The short way first::

    $ bash <(curl -s https://raw.github.com/bretth/django-pavlova-project/master/bootstrap.sh) dessert

First create your project folder and virtualenv environment::

    $ mkproject dessert

To create a new Django project called '**dessert**' using django-pavlova-project, run the following command (this assumes you have Django 1.5 or 1.4 installated aready)::

    $ django-admin.py startproject --template=https://github.com/bretth/django-pavlova-project/zipball/master --extension=py,rst,html,json dessert

You can choose a different name by running the same command but replacing the word '**dessert**' with something else.

Then, depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/dev.txt
    $ ./manage.py syncdb --noinput

A superuser is created by default (in development only) with the login and password ``admin``.

For production::

    $ pip install -r requirements.txt
    
    
Project Template Notes
------------------------
The pavlova project templates is intended for larger projects where the standard django settings can become an anti-pattern. Specifically we're trying to avoid:

 - Long settings files
 - if else DEBUG settings
 - Diverging production and development/testing settings
 - non-versioned local development settings
 - commenting out blocks of settings to switch configuration
 - the settings file shuffle when injecting a new app's configuration, otherwise know as 'where in the world does this setting go'.

Pavlova uses the sqlite3 database for development and testing. If you use any postgresql specific features however, then it stands you should develop and test against the same postgresql version that is in production.

Semantics matter. Class mixins in settings classes named RedisCache and LocalMemCache are more meaningful than ProdCache and DevCache. A glance at ProductionSettings should tell a lot about how the project is configured.

Modular settings matter. Django uses python based settings and django-configurations turns that into class based settings, so your settings.py doesn't need to pretend it's an config.ini file. Modern ide *goto anything* searches are great and all, but breaking your code up into discrete modules is better, and creating multiple alternative mixins without code sprawl is the payoff.

For local app configuration Pavlova recommends defining your defaults in an app_settings.py module in your app's package, and putting any project overrides in it's own <app name>.py module in the settings directory or in a related module settings file and class - i.e. if you have a bunch of custom cache timeouts in different app views then app/app_settings.py and settings/cache.py is where they belong.


Acknowledgements
-----------------

    - The django-pavlova-project draws on the excellent https://github.com/twoscoops/django-twoscoops-project/ for it's thoughtful layout and some base settings.
