#!/bin/bash

## ------------------------
## DESCRIPTION:
## This file is executed when docker starts the django container.
## The purpose is to grab the psotgres host and verify the db.
## ------------------------

# Setup database migrations
cd /opt/Project/project
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic -v0 --noinput

supervisord -n
