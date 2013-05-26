if [ $2 == dev ]; then
    pip install -e git+git://github.com/django/django.git#egg=django
else
    pip install django
fi
django-admin.py startproject --template=https://github.com/bretth/django-pavlova-project/zipball/master --extension=py,rst,html,json,cfg $1 .
pip install -r requirements/dev.txt
chmod +x manage.py
ln -s djangoproject/djangoproject/templates templates
python manage.py syncdb --noinput