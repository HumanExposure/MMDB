
# MDB Metadata REST API



## JSON API REST Framework for the MMDB Metadata

- Based on: https://django-rest-framework-json-api.readthedocs.org/
- Format specification: http://jsonapi.org/format/
- Django REST Framework: https://www.django-rest-framework.org/


## Main Requirements

1. Python (3.8)
2. Django (3.1)
3. Django REST Framework (3.12)


## Setting up and running the MMDB app

Use `conda` to create and activate an environment, as specified in the `environment.yml` file:

```
    $ conda env create -f environment.yml
    $ conda activate mmdb
```
Conda will run `pip install -r [requirementsfile}.txt` for all the files listed in the .yml specifications.

Create a schema in your local MySQL server called `mmdb`.

Migrate and load the data:

```
    $ django-admin migrate --settings=mmdb.settings
    $ django-admin loaddata mmdb --settings=mmdb.settings
    $ django-admin runserver 8002 --settings=mmdb.settings
```

Run tests:

```
django-admin testmmdb.tests --settings=mmdb.settings.test
```
Browse to
* http://localhost:8002 for the list of available collections (in a non-JSONAPI format!),
* http://localhost:8002/swagger-ui/ for a Swagger user interface to the dynamic schema view, or
* http://localhost:8002/openapi for the schema view's OpenAPI specification document.


# Run App with Docker

### .env settings

##### Related settings
* COMPOSE_PROJECT_NAME=mmdb
  <br/> defines the prefix of docker container name
* COMPOSE_FILE
  <br/> defines the compose file to build the service
* MMDB_BRANCH
  <br/> defines the github branch to build from when use docker-compose.override.yaml
* MMDB_PORT=8002
  <br/> defines the port to run the app, defaults to 8002
* SQL_DATABASE=mmdb
* SQL_HOST
* SQL_PORT
* SQL_USER
* SQL_PASSWORD


##### Run with code on local dev machine and mysql on host server

* COMPOSE_FILE=docker/docker-compose.yaml;docker/docker-compose.dev.override.yaml
* SQL_HOST=host.docker.internal

##### Run with code on remote github and mysql on host server
* COMPOSE_FILE=docker/docker-compose.yaml;docker/docker-compose.override.yaml
* SQL_HOST=host.docker.internal
* MMDB_BRANCH=the_remote_branch_name (defaults to master)

##### Run with mysql as a docker service
* COMPOSE_FILE=docker/docker-compose.yaml;docker/docker-compose.dev.override.yaml;docker/docker-compose.mysql.override.yaml
<br/>or</br> 
* COMPOSE_FILE=docker/docker-compose.yaml;docker/docker-compose.override.yaml;docker/docker-compose.mysql.override.yaml
* SQL_HOST=mysql


### Build and run
```
$ docker-compose build
$ docker-compose up
```
Then browse to http://localhost:8002 (or the port configured)


### Apply db migrations
Manually ssh to the mmdb container and run the migrate command
```
$ docker exec -it mmdb_mmdb_1 /bin/sh
# django-admin migrate --settings=mmdb.settings
```