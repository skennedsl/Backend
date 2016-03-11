#!/usr/bin/env bash

echo "Waiting..."

sleep 5;

echo "--> Downloading JSON Parser"
wget http://stedolan.github.io/jq/download/linux64/jq
chmod +x jq

echo "--> Getting Website Api Status"
status=$(curl 'http://localhost:80/api/status/' | ./jq -r '.status')
if [ "$status" == "success" ]; then
  echo "TEST SUCCESS!"
else
  echo "TEST FAILED! $status"; exit 1
fi