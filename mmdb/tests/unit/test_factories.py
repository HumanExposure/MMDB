import pytest

from example.factories import SourceFactory
from example.models import Source

pytestmark = pytest.mark.django_db


def test_factory_instance(source_factory):

    assert source_factory == SourceFactory


def test_model_instance(source):

    assert isinstance(source, Source)

