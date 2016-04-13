#!/bin/bash

PG_PASS=somepass
PG_VERSION=9.5
DEBUG=1
LOCAL=1
DB_EXISTS=0

sudo apt-get update
sudo apt-get install libpq-dev python-dev python-pip build-essential libjpeg-dev

echo " "
echo "Setting up a virtual pip environment"
sudo pip install virtualenv || exit 1;
virtualenv env
source env/bin/activate

echo " "
echo "Installing requirements"
# Files can have spaces. Force the virtualenv interpreter using quotes:
./env/bin/python2.7 ./env/bin/pip install -r ./docker/django/requirements.txt || exit 1;

MEDIA_ROOT=$(pwd)/persistant/media/

mkdir -p MEDIA_ROOT

export LOCAL DEBUG MEDIA_ROOT

SENTINAL=0
while [ $SENTINAL = 0 ]; do
	echo " "
	echo "Migrating the database"
	./env/bin/python2.7 ./project/manage.py makemigrations
	./env/bin/python2.7 ./project/manage.py migrate

	echo " "
	read -r -p "Creating Super User? [y/N] " response
	if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]; then
		./env/bin/python2.7 ./project/manage.py createsuperuser
	fi

	./env/bin/python2.7 ./project/manage.py runserver 0.0.0.0:8000

	echo " "
	read -r -p "Restart Server? [y/N] " response
	if [[ ! $response =~ ^([yY][eE][sS]|[yY])$ ]]
	then
		SENTINAL=1
	fi
done

deactivate

echo " "
read -r -p "Remove Environment Data? [y/N] " response
if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]
then
	sudo rm -rf env/
fi
read -r -p "Remove Database? [y/N] " response
if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]
then
	rm -rf ./project/db.sqlite3
fi

echo " "
echo "Done."
