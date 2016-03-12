[![Circle CI](https://circleci.com/gh/ScribblesProject/Backend.svg?style=svg)](https://circleci.com/gh/ScribblesProject/Backend)

# Installation

1. Install Docker and Docker-compose
2. navigate to this directory in terminal
3. type:

```
PG_PASS=somepass docker-compose up -d
```

## Initial Admin User

You will need to add an initial admin user in order to access the admin portal. Do the following:

```
docker ps 
# find the label for the docker web container
# will call this label currentfolder_web_1 for now
docker exec -ti currentfolder_web_1 bash
> cd /opt/Project/project
> python manage.py createsuperuser
```

## Docker-compose

Rebuild Project

```
docker-compose build
PG_PASS=somepass docker-compose up -d
```

Stop Project

```
docker-compose down
<OR>
docker-compose stop && docker-compose rm
```

## DEBUG

Add the DEBUG flag to all `docker-compose up` commands. Like this:

```
PG_PASS=somepass DEBUG=1 docker-compose up -d
```

## Running Locally

**Requirements:**
- pip
- Docker

**Running:**

```
sudo ./run-local.sh
```

To access, visit `http://localhost:8000`

**What is this thing doing?**

1. Installs and creates a virtualenv - a virtual environment for pip installations. This is so I dont mess with any pip stuff you have currently on your system.
2. Runs a postgres container on port 5432 - Creates a volume, `persistant/`, to store the data
3. Migrates the database
4. Runs a django development server - This allows for files to be modified while the server is running