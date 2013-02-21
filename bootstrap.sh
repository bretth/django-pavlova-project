pip install django
django-admin.py startproject --template=https://github.com/bretth/django-pavlova-project/zipball/master --extension=py,rst,html,json $1
pip install -r $1/requirements/dev.txt
python $1/manage.py syncdb --noinput