from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from rest_framework_json_api.schemas.openapi import SchemaGenerator

from mmdb.views import (
    SourceRelationshipView,
    SourceViewSet,
)

router = routers.DefaultRouter(trailing_slash=False)

router.register(r"sources", SourceViewSet)

urlpatterns = [
    url(r"^", include(router.urls)),
    url(
        r"^sources/(?P<pk>[^/.]+)/relationships/(?P<related_field>\w+)$",
        SourceRelationshipView.as_view(),
        name="source-relationships",
    ),

    path(
        "openapi",
        get_schema_view(
            title="MMDB Metadata API",
            description="API for the Multimedia Monitoring Database …",
            version="1.0.0",
            generator_class=SchemaGenerator,
        ),
        name="openapi-schema",
    ),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r"^__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
