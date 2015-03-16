from .base import *  # noqa

# Local in-memory cache means you can't count on cache invalidation to
# propagate to other servers. If you need it, consider using Memcached
# instead (memcached is always a better option here if you can use it)
# https://docs.djangoproject.com/en/1.7/topics/cache/#memcached

CACHES = {
    'default': {
        'BACKEND': ENV_STR('CACHE_BACKEND',
            'django.core.cache.backends.locmem.LocMemCache'),
        'LOCATION': ENV_STR('CACHE_LOCATION', '')
    }
}

# Log warning and above to console. The console should be redirected to
# a logfile or syslog. Log level can be overridden by environment variable.
# Available levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': ENV_STR('LOG_LEVEL', 'WARNING'),
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] PID:%(process)d %(levelname)s '
                '%(pathname)s:%(lineno)d: %(message)s'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': ENV_STR('LOG_LEVEL', 'WARNING'),
            'propagate': True
        }
    }
}
