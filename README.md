# **Objective**: Build OxBot ENV

## Step 1: Create a clean Dockerfile with latest Python3, Djago and PostgreSQL

Try to use a clean image that offers the bear minimum to run the docker successfully.

```Dockerfile
# syntax=docker/dockerfile:1

# Starts with a Python3 parent image
FROM python:3

# Setting env configs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Creates a working directory. (Note: This is the directory created inside of the build image)
WORKDIR /code

# Saves dependencies to a single file. Similar to package.json or composer
COPY requirements.txt /code/

# Install dependencies during the build
RUN pip install -r requirements.txt

# Copy everthign in currente dir to container code dir
COPY . /code/
```

## Step 2: Create a file called docker-compose.yml in the root directory

The docker-compose.yml file describes the services in the app. At the beginning a web server and database are only added. This file also describes which Docker images these services use, how they link together, any volumes they might need to be mounted inside the containers. Finally, the file describes which ports these services expose to.

```yml
version: "3.9" # lastest version as of now

services:
  web:
    build: . # build from root Dockerfile
    command: python manage.py runserver 0.0.0.0:8000 # django local server port
    volumes:
      - .:/code # mount current dir to /code in the container
    ports:
      - "8000:8000" # connect local port 8000 with containers
    environment: # connect web app with db with same credentials. note: need to be refactored for security reason a bit later.
      - POSTGRES_NAME=OxBot-main
      - POSTGRES_USER=OxBotAdmin
      - POSTGRES_PASSWORD=gDmuZQPg!Einps2mqPCy
    depends_on:
      - db
  db:
    image: postgres # lastest postgres
    volumes:
      - ./data/db:/var/lib/postgresql/data # local db volumne mount
    environment: # sample credentials
      - POSTGRES_DB=OxBot-main
      - POSTGRES_USER=OxBotAdmin
      - POSTGRES_PASSWORD=gDmuZQPg!Einps2mqPCy
```

## Step 3: Create a Django Project

Create a Django starter project by building the image from the build context defined in the previous procedures.

1. Change to the root of your project directory.
2. Create the Django project by running the docker-compose run command as follows.

```sh
sudo docker-compose run web django-admin startproject OxBot .
```

This allows docker-compose to run django-admin startproject OxBot (the project name) in a container, using the web service’s image and configuration. Because the web image doesn’t exist yet, Compose builds it from the current directory, as specified by the build: . line in docker-compose.yml.

Once the web service image is built, Compose runs it and executes the django-admin startproject command in the container. This command instructs Django to create a set of files and directories representing OxBot, a Django project.

## Step 4: Connect to the database

In The project directory, edit the OxBot/settings.py file.
Replace the DATABASES = ... with the following:

```py
import os

[...]

ALLOWED_HOSTS = ['0.0.0.0']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

These settings are determined by the postgres Docker image specified in docker-compose.yml.

## Step 5: Run the docker-compose up command

```sh
docker-compose up
```

## issues

Invalid HTTP_HOST header: '0.0.0.0:8000'. You may need to add '0.0.0.0' to ALLOWED_HOSTS
Just add the ip in ALLOWED_HOSTS property in the file <your_app_path>/settings.py.

## References

- [Docker Official Reference - Django and PostgreSQL](https://docs.docker.com/samples/django/)
