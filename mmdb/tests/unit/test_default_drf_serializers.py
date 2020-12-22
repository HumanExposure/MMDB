import json
from datetime import datetime

import pytest
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from rest_framework_json_api.renderers import JSONRenderer

from mmdb.models import Source


@pytest.mark.django_db
def test_source_create(client):

    url = reverse("drf-source-list")
    name = "Dummy Name"

    request_data = {
        "data": {"attributes": {"name": name}, "type": "source"},
    }

    resp = client.post(url, request_data)

    # look for created source in database
    source = Source.objects.filter(name=name)

    # check if source exists in database
    assert source.count() == 1

    # get created source from database
    source = source.first()

    expected = {
        "data": {
            "attributes": {"name": source.name, "tags": []},
            "id": "{}".format(source.id),
            "links": {"self": "http://testserver/source/{}".format(source.id)},
            "type": "sources",
        },
        "meta": {"apiDocs": "/docs/api/sources"},
    }

    assert resp.status_code == 201
    assert resp.json() == expected


@pytest.mark.django_db
def test_get_object_gives_correct_source(client, source):

    url = reverse("drf-source-detail", kwargs={"source_pk": source.id})
    resp = client.get(url)
    expected = {
        "data": {
            "attributes": {"name": source.name, "tags": []},
            "id": "{}".format(source.id),
            "links": {"self": "http://testserver/sources/{}".format(source.id)},
            "meta": {"copyright": datetime.now().year},
            "type": "sources",
        },
        "meta": {"apiDocs": "/docs/api/sources"},
    }
    got = resp.json()
    assert got == expected


@pytest.mark.django_db
def test_get_object_patches_correct_source(client, source):

    url = reverse("drf-source-detail", kwargs={"source_pk": source.id})
    new_name = source.name + " update"
    assert not new_name == source.name

    request_data = {
        "data": {
            "attributes": {"name": new_name},
            "id": "{}".format(source.id),
            "links": {"self": "http://testserver/sources/{}".format(source.id)},
            "meta": {"copyright": datetime.now().year},
            "type": "sources",
        },
        "meta": {"apiDocs": "/docs/api/sources"},
    }

    resp = client.patch(url, data=request_data)

    assert resp.status_code == 200

    expected = {
        "data": {
            "attributes": {"name": new_name, "tags": []},
            "id": "{}".format(source.id),
            "links": {"self": "http://testserver/sources/{}".format(source.id)},
            "meta": {"copyright": datetime.now().year},
            "type": "sources",
        },
        "meta": {"apiDocs": "/docs/api/sources"},
    }
    got = resp.json()
    assert got == expected


@pytest.mark.django_db
def test_get_object_deletes_correct_source(client, entry):

    url = reverse("drf-source-detail", kwargs={"source_pk": source.id})

    resp = client.delete(url)

    assert resp.status_code == 204
