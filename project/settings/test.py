from .base import *  # noqa
from uuid import uuid4

# For tests, usually we can generate new secret key every time. Sometimes
# (when using SQL-level fixtures with session information) you may want to
# provide the value instead
SECRET_KEY = ENV_STR('SECRET_KEY', uuid4().hex)

# Use in-memory SQLIte3 database for faster tests. Great for starting, but
# at some point you should be using your production database engine (e.g.
# PostgreSQL) for tests as well, as the db engine behaviour differs noticably
DATABASES = {
    'default': dj_database_url.config(default='sqlite://:memory:')
}

# Use insecure but faster password hasher to avoid unneccessarily slowing down
# tests
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
