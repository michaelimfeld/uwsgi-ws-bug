#!/bin/sh

/usr/local/bin/uwsgi --http :8080 --http-websockets --wsgi-file wsgi.py --processes 1 --threads 100 --master
