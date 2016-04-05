#!/usr/bin/env bash

echo " "
echo "Pulling Latest Changes"
ssh $DEPLOY_USER@$DEPLOY_HOST "cd ~/Class/csc190/backend; git reset --hard HEAD; git pull --rebase origin master"

echo " "
echo "Docker-compose pulling"
ssh $DEPLOY_USER@$DEPLOY_HOST "cd ~/Class/csc190/backend; docker-compose pull"

echo " "
echo "Docker-compose building"
ssh $DEPLOY_USER@$DEPLOY_HOST "cd ~/Class/csc190/backend; docker-compose build;"

echo " "
echo "Docker-compose running postgres"
ssh $DEPLOY_USER@$DEPLOY_HOST "PG_PASS=$DEPLOY_POSTGRES_PASS docker-compose up -d postgres"

echo " "
echo "Waiting to ensure postgres is ready... 15 sec"
sleep 15

echo " "
echo "Docker-compose running postgres"
ssh $DEPLOY_USER@$DEPLOY_HOST "PG_PASS=$DEPLOY_POSTGRES_PASS docker-compose up -d django"

