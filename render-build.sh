#!/usr/bin/env bash
python manage.py migrate --noinput
gunicorn core.wsgi