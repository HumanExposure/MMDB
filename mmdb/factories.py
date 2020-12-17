# -*- encoding: utf-8 -*-

import factory
from faker import Factory as FakerFactory

from mmdb.models import (
    Source,
)

faker = FakerFactory.create()
faker.seed(983843)


class SourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Source

