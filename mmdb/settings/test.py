from .dev import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "mmdb.urls"

JSON_API_FORMAT_FIELD_NAMES = "camelize"
JSON_API_FORMAT_TYPES = "camelize"
JSON_API_PLURALIZE_TYPES = True

REST_FRAMEWORK.update(
    {  # noqa
        "PAGE_SIZE": 1,
    }
)