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

When doing development, it kind of sucks to have to rebuild every time something changes. Use the LOCAL docker-compose file to force the docker contianer to use the same file system as the current directory. This way any changes made will update the server automatically (unless its a change to settings.py).

To run the alternative docker-compose:

```
PG_PASS=somepass DEBUG=1 docker-compose -f ./docker-compose_LOCAL.yml up -d
```

If you make a change to a django setting, you will need to restart the service:

```
docker-compose restart web
```