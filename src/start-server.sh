#!/usr/bin/env bash

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd books; python manage.py createsuperuser --no-input)
fi
(cd books; gunicorn books.wsgi --user www-data --bind 127.0.0.1:8010 --workers 9) & nginx -g "daemon off;"
