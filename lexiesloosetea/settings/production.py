import os
from .base import *

DEBUG = False
SECRET_KEY = 'i)hncbk8oo2!b_6_b7_ka30&&*#+l76w$c=f!ff@5157)rhz3*'
ALLOWED_HOSTS = ['localhosts', 'lexiesloosetea.ca', '*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql.psycopg2',
        'NAME': 'lexiesloosetea',
        'USER': 'lexiesloosetea',
        'PASSWORD': 'residentevil808',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://222d12286c4642299cdad51907ee77f3@o511268.ingest.sentry.io/5608545",
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
