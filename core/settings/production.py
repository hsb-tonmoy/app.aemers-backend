import os
from .development import *
import dj_database_url

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

DEBUG = False
SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', False)

ALLOWED_HOSTS = ['api.aemers.com', '127.0.0.1', '0.0.0.0',
                 'localhost', 'appaemers.onrender.com']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
