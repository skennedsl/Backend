CircleCI - [![Circle CI](https://circleci.com/gh/ScribblesProject/Backend.svg?style=svg)](https://circleci.com/gh/ScribblesProject/Backend)

# Running Locally

**Requirements:**

- Python
- pip
- Docker (for server deployment)
- Docker-compose (for server deployment)

**Running Locally:**

On Linux and OSX (EASIEST):

```
sudo ./run-local.sh
```

Other:

```
cd Backend

# make a media folder to store local uploads in 
# MAKE SURE THIS FOLDER DOES NOT END UP IN GIT PLEASE
# Because of this just make it on your desktop
mkdir ~/Desktop/backend-media

# Install Python Dependencies
pip install -r ./docker/django/requirements.txt

# you will need 3 environment variables for things to work
# - MEDIA_ROOT (that folder from before)
# - DEBUG (to show debug logs)
# - LOCAL (indicating to use a local db)
# These will appear before each of the following calls

# Setup DB
MEDIA_ROOT=~/Desktop/backend-media LOCAL=1 DEBUG=1 python manage.py makemigrations
MEDIA_ROOT=~/Desktop/backend-media LOCAL=1 DEBUG=1 python manage.py migrate

# Create a superuser 
MEDIA_ROOT=~/Desktop/backend-media LOCAL=1 DEBUG=1 python manage.py createsuperuser

# Start the server
MEDIA_ROOT=~/Desktop/backend-media LOCAL=1 DEBUG=1 python manage.py runserver
```

To access, visit `http://localhost:8000`

# Installation On Server

1. Install Docker and Docker-compose
2. navigate to this directory in terminal
3. type:

```
PG_PASS=somepass docker-compose up -d postgres

# allow time for postgres to come up
sleep 15

PG_PASS=somepass docker-compsoe up -d django
```

Verify by viditing http://localhost

## Setup Initial Admin User (on server)

First use the above settings to get things up and running. 
You will need to add an initial admin user in order to access the admin portal. Do the following:

```
docker ps 
# find the label for the docker django container

# the next call executes starts an instance of the django server
#  and starts an interactive bash shell
docker exec -ti currentfolder_django_1 bash

# in the bash shell, navigate to where the code was copied to. 
# (see Docker file in ./docker/django/Dockerfile)
> cd /opt/Project/project

# Now create the super user
# the environment variables should already be present (see Dockerfile)
> python manage.py createsuperuser
```

## Docker-compose (on server)

Rebuild Project. (if its already running). Dont stop it. IF ITS NOT ALREADY RUNNING, SEE "Installation On Server"

```
docker-compose build
PG_PASS=somepass docker-compose up -d 
```

Stop Project

```
docker-compose stop && docker-compose rm
```

## DEBUG

Add the DEBUG flag to all `docker-compose up` commands. Like this:

```
PG_PASS=somepass DEBUG=1 docker-compose up -d
```
