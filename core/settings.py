import os
from .secrets import SECRET_KEY, BASE_DIR, DATABASES

ALLOWED_HOSTS = []

DEBUG = True

ROOT_URLCONF = "core.urls"

INSTALLED_APPS = [
 "django.contrib.contenttypes",
 "django.contrib.staticfiles",
 "sass_processor",
 "core"
]

DATE_FORMAT = "D j M, Y"
USE_TZ = True
TIME_ZONE = "UTC"

MIDDLEWARE = [
 "django.middleware.common.CommonMiddleware",
]

TEMPLATES = [{
 "BACKEND": "django.template.backends.django.DjangoTemplates",
 "APP_DIRS": True,
 "OPTIONS": {
  "context_processors": [
   "django.template.context_processors.request",
  ],
 },
}]

STATIC_URL = "/static/"
