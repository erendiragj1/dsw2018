#!/bin/bash
#export REQUESTS_CA_BUNDLE="/tmp/srv_monitoreo_cert.crt"

sleep 15

python3 -u manage.py makemigrations
python3 -u manage.py migrate
gunicorn --bind :8000 adminServer.wsgi:application --reload
#python3 -u manage.py runserver 0.0.0.0:8000

