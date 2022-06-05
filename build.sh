#!/usr/bin/env bash

# create the django project
sudo docker-compose run web django-admin startproject $1 .

# change settings.py file (will work on this later since the link and other thing might be different when deploying to cloud)