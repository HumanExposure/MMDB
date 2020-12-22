import rest_framework.exceptions as exceptions
import rest_framework.parsers
import rest_framework.renderers
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

import rest_framework_json_api.metadata
import rest_framework_json_api.parsers
import rest_framework_json_api.renderers
from rest_framework_json_api.django_filters import DjangoFilterBackend
from rest_framework_json_api.filters import (
    OrderingFilter,
    QueryParameterValidationFilter,
)
from rest_framework_json_api.pagination import JsonApiPageNumberPagination
from rest_framework_json_api.utils import format_drf_errors
from rest_framework_json_api.views import ModelViewSet, RelationshipView

from mmdb.models import Source
from mmdb.serializers import (
    SourceSerializer,
)

HTTP_422_UNPROCESSABLE_ENTITY = 422


class SourceViewSet(ModelViewSet):
    queryset = Source.objects.all()
    resource_name = "sources"
    serializer_class = SourceSerializer

class SourceRelationshipView(RelationshipView):
    queryset = Source.objects.all()