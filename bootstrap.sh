pip install django
django-admin.py startproject --template=https://github.com/bretth/django-pavlova-project/zipball/master --extension=py,rst,html,json $1 .
pip install -r requirements/dev.txt
chmod +x manage.py
python manage.py syncdb --noinput