#!/bin/sh
function help {
echo "Usage: ./bootstrap.sh <project_name> [--dev]"
}

PR="==> "

DJANGO="pip install django"
if [ $# -eq 2 ]; then
        if [ $2 == --dev ]; then
                DJANGO="pip install -e git+git://github.com/django/django.git#egg=django"
        else
                echo "Invalid argument"
                help
                exit 1
        fi
fi
if [ $# -eq 0 -o $# -gt 2 ]; then 
        help
        exit
fi

echo $PR$DJANGO
$DJANGO
echo
SP="django-admin.py startproject --template=https://github.com/bretth/django-pavlova-project/zipball/master --extension=py,rst,html,json,cfg $1 ."
echo $PR$SP
$SP
echo
REQ="pip install -r requirements/dev.txt"
echo $PR$REQ
$REQ
echo
SYNC="python manage.py syncdb --noinput"
echo $PR$SYNC
$SYNC
echo
CH="chmod +x manage.py"
echo $PR$CH
$CH

