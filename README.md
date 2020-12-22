
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
Browse to
* http://localhost:8002 for the list of available collections (in a non-JSONAPI format!),
* http://localhost:8002/swagger-ui/ for a Swagger user interface to the dynamic schema view, or
* http://localhost:8002/openapi for the schema view's OpenAPI specification document.

