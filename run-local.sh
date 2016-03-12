#!/bin/bash

PG_PASS=somepass
PG_VERSION=9.5
DEBUG=1
DB_EXISTS=0

echo " "
echo "Setting up a virtual pip environment"
sudo pip install virtualenv || exit 1;
virtualenv env
source env/bin/activate

if [ -d "`pwd`/persistant/postgresdata-$PG_VERSION" ]; then
	DB_EXISTS=1
fi

echo " "
echo "Installing requirements"
# Files can have spaces. Force the virtualenv interpreter using quotes:
./env/bin/python2.7 ./env/bin/pip install -r ./docker/django/requirements.txt || exit 1;

echo " "
echo "Removing previous local docker instances"
docker stop postgres_local
docker rm postgres_local

echo " "
echo "Starting Postgres"
PG_REPO=mdillon/postgis
docker pull $PG_REPO:$PG_VERSION || exit 1;
docker run -v "`pwd`/persistant/postgresdata-$PG_VERSION":"/data" -p 5432:5432 -e POSTGRES_PASSWORD=$PG_PASS -e PGDATA=/data/main -d --name postgres_local $PG_REPO:$PG_VERSION

echo " "
echo "Waiting for postgres to start (15 sec)"
COUNTER=0
while [  $COUNTER -lt 15 ]; do
	printf "."
	let COUNTER=COUNTER+1
	sleep 1
done
echo " "

PG_HOST=$(docker port postgres_local | awk -F"-> " '{ print $2 }' | awk -F: '{ print $1 }')
PG_PORT=$(docker port postgres_local | awk -F"-> " '{ print $2 }' | awk -F: '{ print $2 }')

export PG_HOST PG_PORT PG_PASS DEBUG

SENTINAL=0
while [ $SENTINAL = 0 ]; do
	echo " "
	echo "Migrating the database"
	./env/bin/python2.7 ./project/manage.py makemigrations
	./env/bin/python2.7 ./project/manage.py migrate

	if [ $DB_EXISTS = 0 ]; then 
		echo " "
		echo "Create initial super user"
		./env/bin/python2.7 ./project/manage.py createsuperuser	
		DB_EXISTS=1
	fi

	./env/bin/python2.7 ./project/manage.py runserver 0.0.0.0:8000

	echo " "
	read -r -p "Restart Server? [y/N] " response
	if [[ ! $response =~ ^([yY][eE][sS]|[yY])$ ]]
	then
		SENTINAL=1
	fi
done

#Clean up
echo " "
echo "Stopping Postgres"
docker stop postgres_local
docker rm postgres_local
deactivate

echo " "
read -r -p "Remove Environment Data? [y/N] " response
if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]
then
	sudo rm -rf env/
fi
read -r -p "Remove Postgres Data? [y/N] " response
if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]
then
	sudo rm -rf persistant/
fi

echo " "
echo "Done."