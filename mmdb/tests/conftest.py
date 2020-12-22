import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from mmdb.factories import (
    SourceFactory
)

register(SourceFactory)



@pytest.fixture
def single_source(source):

    source = source_factory()
    return source


@pytest.fixture
def multiple_sources(source_factory):

    sources = [
        source_factory(),
        source_factory(),
    ]
    return sources


@pytest.fixture
def client():
    return APIClient()
