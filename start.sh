#!/bin/bash

python3 manage.py makemigrations posts
python3 manage.py migrate
python3 manage.py collectstatic --noinput

gunicorn tweety.wsgi
