import pytest

from mmdb.factories import SourceFactory
from mmdb.models import Source

pytestmark = pytest.mark.django_db


def test_factory_instance(source_factory):

    assert source_factory == SourceFactory


def test_model_instance(source):

    assert isinstance(source, Source)
