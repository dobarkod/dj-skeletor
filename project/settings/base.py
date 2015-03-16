# Base settings for Django project
import os
from .env import ENV_BOOL, ENV_STR, ENV_LIST

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def ABS_PATH(*args):  # noqa
    return os.path.join(BASE_DIR, *args)

SECRET_KEY = ENV_STR('SECRET_KEY', '')
DEBUG = ENV_BOOL('DEBUG', False)
TEMPLATE_DEBUG = ENV_BOOL('TEMPLATE_DEBUG', DEBUG)
ALLOWED_HOSTS = ENV_LIST('ALLOWED_HOSTS', ',', [])

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'

import dj_database_url
DATABASES = {'default': dj_database_url.config()}

LANGUAGE_CODE = ENV_STR('LANGUAGE_CODE', 'en-us')
TIME_ZONE = ENV_STR('TIME_ZONE', 'UTC')
USE_I18N = ENV_BOOL('USE_I18N', True)
USE_L10N = ENV_BOOL('USE_L10N', True)
USE_TZ = ENV_BOOL('USE_TZ', True)

STATIC_URL = ENV_STR('STATIC_URL', '/static/')
STATIC_ROOT = ENV_STR('STATIC_ROOT', ABS_PATH('static'))

MEDIA_URL = ENV_STR('MEDIA_URL', '/media/')
MEDIA_ROOT = ENV_STR('MEDIA_ROOT', ABS_PATH('media'))

TEMPLATE_DIRS = (
    ABS_PATH('templates'),
)

COMPRESS_ENABLED = ENV_BOOL('COMPRESS_ENABLED', not DEBUG)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
