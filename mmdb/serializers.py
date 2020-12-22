
from rest_framework import serializers as drf_serializers

from mmdb.models import (
    Source
)


class SourceSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'
