#!/bin/sh

nginx

# This will exec the CMD from your Dockerfile, i.e. "npm start"

uwsgi --ini /var/www/python-intro/intro/uwsgi.ini