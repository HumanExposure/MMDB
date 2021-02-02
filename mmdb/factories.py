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

    name = factory.LazyAttribute(lambda x: faker.lexify(text="?????"))
    description = factory.LazyAttribute(lambda x: faker.lexify(text="???????"))
    who = factory.LazyAttribute(lambda x: faker.lexify(text="?????"))
    type = factory.LazyAttribute(lambda x: faker.text(30))
    oppt_phase = factory.LazyAttribute(lambda x: faker.random_int(min=0, max=7))
    processed = 1
    harm_init = 1
    harm_mapped = 1
    loaded = 1
    full_source_name = factory.LazyAttribute(lambda x: faker.lexify(text="?????"))
