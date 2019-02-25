#!/bin/sh

while ! pg_isready -h pydemodb -p 5432 -U pydemo
do
    sleep 3
done

python manage.py migrate
python manage.py makemigrations
gunicorn --bind 0.0.0.0:8000 --workers 5 demosolst.wsgi:application