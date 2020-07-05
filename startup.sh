#!/usr/bin/env bash
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py runserver 0.0.0.0:80

# gunicorn xunjian.wsgi:application -c gunicorn_conf.py