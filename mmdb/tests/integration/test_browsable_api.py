import re

import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_browsable_api(single_source, client):
    response = client.get(
        reverse("source-detail", kwargs={"pk": single_source.pk, "format": "api"})
    )
    content = str(response.content)
    assert response.status_code == 200
    assert re.search(r"JSON:API includes", content)
    assert re.search(
        r'<input type="checkbox" name="includes" [^>]* value="description"', content
    )

