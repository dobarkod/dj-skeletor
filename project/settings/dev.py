from .base import *  # noqa
from uuid import uuid4

DEBUG = ENV_BOOL('DEBUG', True)
TEMPLATE_DEBUG = ENV_BOOL('TEMPLATE_DEBUG', DEBUG)
ALLOWED_HOSTS = ENV_LIST('ALLOWED_HOSTS', ',', ['*'])

# In development, we usually don't need to have a hardcoded secret key. If
# it's needed, you can provide it via environment variable.
SECRET_KEY = ENV_STR('SECRET_KEY', uuid4().hex)

EMAIL_BACKEND = ENV_STR('EMAIL_BACKEND',
    'django.core.mail.backends.console.EmailBackend')

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + ABS_PATH('dev.db'))
}

# Disable caching while in development
CACHES = {
    'default': {
        'BACKEND': ENV_STR('CACHE_BACKEND',
            'django.core.cache.backends.dummy.DummyCache'),
        'LOCATION': ENV_STR('CACHE_LOCATION', '')
    }
}

# Available levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': ENV_STR('LOG_LEVEL', 'INFO'),
            'class': 'logging.StreamHandler',
        }
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': ENV_STR('LOG_LEVEL', 'INFO'),
            'propagate': True
        }
    }
}

QUERY_INSPECT_ENABLED = True
QUERY_INSPECT_LOG_STATS = True
QUERY_INSPECT_HEADER_STATS = True
QUERY_INSPECT_LOG_QUERIES = True
# Whether to include tracebacks in the logs (default: False)
QUERY_INSPECT_LOG_TRACEBACKS = True
# Project root (one or several colon-separated directories, default empty)
QUERY_INSPECT_TRACEBACK_ROOTS = [
    BASE_DIR
]
