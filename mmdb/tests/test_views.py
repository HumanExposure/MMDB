import json
from datetime import datetime

from django.test import RequestFactory
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate

from rest_framework_json_api import serializers, views
from rest_framework_json_api.utils import format_resource_type

from mmdb.factories import SourceFactory
from mmdb.models import Source
from mmdb.serializers import (
    SourceSerializer,
)
from mmdb.tests import TestBase
from mmdb.views import SourceViewSet


class TestModelViewSet(TestBase):
    def setUp(self):
        self.source = SourceFactory.create()

    def test_no_content_response(self):
        url = "/sources/{}".format(self.source.pk)
        response = self.client.delete(url)
        assert response.status_code == 204, response.rendered_content.decode()
        assert len(response.rendered_content) == 0, response.rendered_content.decode()
