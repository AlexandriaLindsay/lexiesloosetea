import os
from .base import *

DEBUG = False
SECRET_KEY = '=h1+*y3r8+r6a1=1u&4f%*40^y#5x6e5+$(z#5e!%5f3ce*_ue'
ALLOWED_HOSTS = ['localhost', 'lexiesloosetea.ca', '*'] 

cwd = os.getcwd()
CACHES = {
    {
        "default": {
            "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
            "LOCATION": f"{cwd}/.cache"
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lexiesloosetea',
        "USER": 'lexiesloosetea',
        "PASSWORD": 'residentevil808@',
        "HOST": 'localhost',
        "PORT": "",
    }
}


import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://92a0403ba89f4ec68deba440e0e63d09@o511268.ingest.sentry.io/5608162",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass
